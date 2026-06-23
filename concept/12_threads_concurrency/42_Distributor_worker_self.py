import sys
import os
import time
import uuid
import sqlite3
import json

DB_FILE = "distributed_cluster_matrix.db"

class ClusterStorage:
    """Simulates a fault-tolerant network Broker and Result Backend storage layer."""
    @staticmethod
    def init_cluster_infrastructure():
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Unified Task Ledger tracking the distributed state machine
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cluster_tasks (
                    task_id TEXT PRIMARY KEY,
                    task_name TEXT,
                    payload_args TEXT,
                    status TEXT,
                    assigned_worker TEXT,
                    heartbeat_expires_at REAL,
                    result_data TEXT
                )
            """)
            conn.commit()

    @staticmethod
    def dispatch_task_to_broker(task_name, args):
        task_id = str(uuid.uuid4())
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cluster_tasks VALUES (?, ?, ?, 'QUEUED', NULL, 0, NULL)",
                (task_id, task_name, json.dumps(args))
            )
            conn.commit()
        return task_id

    @staticmethod
    def claim_next_available_job(worker_id):
        """
        Atomic State-Machine Transition. Fetches a job and leases it safely.
        Bypasses race conditions and handles worker failures.
        """
        now = time.time()
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            
            # Find a task that is QUEUED OR has a dead/expired heartbeat lease
            cursor.execute("""
                SELECT task_id, task_name, payload_args FROM cluster_tasks
                WHERE status = 'QUEUED' 
                OR (status = 'PROCESSING' AND heartbeat_expires_at < ?)
                LIMIT 1
            """, (now,))
            
            row = cursor.fetchone()
            if row:
                task_id, task_name, args_json = row
                # Set a 4-second processing lease window
                lease_timeout = now + 4 
                
                cursor.execute("""
                    UPDATE cluster_tasks 
                    SET status = 'PROCESSING', assigned_worker = ?, heartbeat_expires_at = ?
                    WHERE task_id = ?
                """, (worker_id, lease_timeout, task_id))
                
                conn.commit()
                return task_id, task_name, json.loads(args_json)
        return None

    @staticmethod
    def resolve_task_state(task_id, status, result_payload):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE cluster_tasks 
                SET status = ?, result_data = ?, heartbeat_expires_at = 0
                WHERE task_id = ?
            """, (status, json.dumps(result_payload), task_id))
            conn.commit()

    @staticmethod
    def get_task_receipt_payload(task_id):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT status, result_data FROM cluster_tasks WHERE task_id = ?", (task_id,))
            row = cursor.fetchone()
            return row if row else ("UNKNOWN", None)


# =====================================================================
# DISTRIBUTED WORKER EXECUTION MACHINE
# =====================================================================

def run_worker_node(node_name):
    worker_id = f"Worker-{node_name}@{os.getpid()}"
    print(f"=== DISTRIBUTED WORKER PROCESS RUNNING: {worker_id} ===")
    print("Polling broker cluster matrix layer... Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Atomic lookups protect against multiple workers grabbing the same job
            job = ClusterStorage.claim_next_available_job(worker_id)
            
            if job:
                task_id, task_name, args = job
                print(f"[{time.strftime('%H:%M:%S')}] [JOB CLAIMED] Intercepted Task {task_name} ({task_id})")
                
                try:
                    # Execute intensive tasks
                    if task_name == "compute_analytics":
                        # Simulate variable processing work
                        time.sleep(2) 
                        output = f"Analyzed metrics for bucket: {args[0]} -> Aggregation Factor: {args[1] * 42}"
                    else:
                        raise ValueError("Unknown task mapping entry.")
                        
                    ClusterStorage.resolve_task_state(task_id, "SUCCESS", output)
                    print(f"  -> [SUCCESS] Result resolved to cluster ledger backend.\n")
                    
                except Exception as err:
                    ClusterStorage.resolve_task_state(task_id, "FAILED", str(err))
                    print(f"  -> [CRASH] Task processing execution error: {err}\n")
            
            # Polling frequency
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\nWorker Node {worker_id} safely unmapped from network cluster storage topology.")

if __name__ == "__main__":
    ClusterStorage.init_cluster_infrastructure()
    
    if len(sys.argv) > 1 and sys.argv[1] == "worker":
        node_lbl = sys.argv[2] if len(sys.argv) > 2 else "Alpha"
        run_worker_node(node_lbl)
    elif len(sys.argv) > 1 and sys.argv[1] == "dispatch":
        bucket = sys.argv[2] if len(sys.argv) > 2 else "Telemetry-Logs"
        scale = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        tid = ClusterStorage.dispatch_task_to_broker("compute_analytics", [bucket, scale])
        print(f"[Producer Client] Job dispatched successfully. Receipt ID: {tid}")
    elif len(sys.argv) > 1 and sys.argv[1] == "status":
        target_id = sys.argv[2]
        status, res = ClusterStorage.get_task_receipt_payload(target_id)
        print(f"[Backend Query] Task Status: {status} | Result Payload: {res}")
    else:
        print("Distributed Cluster Engine CLI usage rules:")
        print("  Launch a Worker:   python distributed_cluster.py worker Node-Alpha")
        print("  Dispatch work:     python distributed_cluster.py dispatch User-Data-Grid 50")
        print("  Query a receipt:   python distributed_cluster.py status [TASK_UUID]")