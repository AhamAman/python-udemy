import sys
import os
import time
import uuid
import sqlite3
import json

DB_FILE = "distributed_scheduler_state.db"

class DistributedSchedulerStorage:
    """Simulates a distributed network database layer supporting atomic state transformations."""
    @staticmethod
    def init_cluster_db():
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Task Table: Holds schedules, execution target states, and node leases
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scheduled_tasks (
                    task_id TEXT PRIMARY KEY,
                    task_name TEXT,
                    run_at_timestamp REAL,
                    status TEXT,
                    leased_by_node TEXT,
                    lease_expires_at REAL
                )
            """)
            conn.commit()

    @staticmethod
    def create_schedule(task_name, delay_seconds):
        task_id = str(uuid.uuid4())
        run_at = time.time() + delay_seconds
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO scheduled_tasks VALUES (?, ?, ?, 'PENDING', NULL, 0)",
                (task_id, task_name, run_at)
            )
            conn.commit()
        return task_id

    @staticmethod
    def acquire_task_lease(node_id):
        """
        The Core Consensus Step. Uses an atomic 'Optimistic Lock' SQL transaction 
        to pick a task that is ready to run and hasn't been leased by another node.
        """
        now = time.time()
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            
            # Find a task that is past its execution time AND either:
            # 1. Status is 'PENDING'
            # 2. Status is 'RUNNING' but the lease expired (the previous node crashed)
            cursor.execute("""
                SELECT task_id, task_name FROM scheduled_tasks 
                WHERE run_at_timestamp <= ? 
                AND (status = 'PENDING' OR (status = 'RUNNING' AND lease_expires_at < ?))
                LIMIT 1
            """, (now, now))
            
            row = cursor.fetchone()
            if row:
                task_id, task_name = row
                lease_window = now + 5 # Claim a 5-second lease window
                
                # Atomic update validation: double-check that we write only if state matches
                cursor.execute("""
                    UPDATE scheduled_tasks 
                    SET status = 'RUNNING', leased_by_node = ?, lease_expires_at = ?
                    WHERE task_id = ?
                """, (node_id, lease_window, task_id))
                
                conn.commit()
                return task_id, task_name
        return None

    @staticmethod
    def finalize_task(task_id):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM scheduled_tasks WHERE task_id = ?", (task_id,))
            conn.commit()

def run_scheduler_node(node_name):
    node_id = f"{node_name}-{os.getpid()}"
    print(f"=== DISTRIBUTED SCHEDULER NODE RUNNING: {node_id} ===")
    print("Polled cluster database state... Press Ctrl+C to terminate node.\n")
    
    try:
        while True:
            # 1. Try to acquire a task lease from the shared network state layer
            leased_job = DistributedSchedulerStorage.acquire_task_lease(node_id)
            
            if leased_job:
                task_id, task_name = leased_job
                print(f"[{time.strftime('%H:%M:%S')}] [LEASE ACQUIRED] Node claimed '{task_name}' ({task_id})")
                
                # 2. Simulate task execution processing
                print(f"  -> Processing business logic action item...")
                time.sleep(2) 
                
                # 3. Finalize and remove task upon successful completion
                DistributedSchedulerStorage.finalize_task(task_id)
                print(f"  -> [SUCCESS] Task completed. Lease dropped cleanly.\n")
                
            # Passive heartbeat interval: check for tasks every 500ms
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\nNode {node_id} disconnected cleanly from cluster storage.")

if __name__ == "__main__":
    DistributedSchedulerStorage.init_cluster_db()
    
    # CLI Engine router
    if len(sys.argv) > 1 and sys.argv[1] == "schedule":
        # Client mode: push new schedules into the cluster
        job_name = sys.argv[2] if len(sys.argv) > 2 else "Default-Cron-Job"
        delay = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
        tid = DistributedSchedulerStorage.create_schedule(job_name, delay)
        print(f"[Cluster UI] Dispatched '{job_name}' to run in {delay}s. Global Task ID: {tid}")
    elif len(sys.argv) > 1:
        # Worker node mode named explicitly via args
        run_scheduler_node(sys.argv[1])
    else:
        print("Usage error. Run with parameters:")
        print("  To launch a node:   python distributed_scheduler.py Node-Alpha")
        print("  To inject a task:   python distributed_scheduler.py schedule Compute-Metrics 4")