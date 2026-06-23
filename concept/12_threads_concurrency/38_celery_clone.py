import sys
import os
import time
import uuid
import sqlite3
import json

DB_FILE = "simulated_network_broker.db"

class BrokerDB:
    """Simulates a network-based Message Broker & Result Backend using SQLite file locking."""
    @staticmethod
    def init_db():
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Table 1: The Outbound Task Queue Buffer
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS task_queue (
                    id TEXT PRIMARY KEY,
                    task_name TEXT,
                    args TEXT
                )
            """)
            # Table 2: The Distributed Result Backend Storage
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS task_results (
                    id TEXT PRIMARY KEY,
                    status TEXT,
                    result TEXT
                )
            """)
            conn.commit()

    @staticmethod
    def push_task(task_name, args):
        task_id = str(uuid.uuid4())
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO task_queue VALUES (?, ?, ?)",
                (task_id, task_name, json.dumps(args))
            )
            # Register the task as pending in the result backend
            cursor.execute(
                "INSERT INTO task_results VALUES (?, 'PENDING', NULL)",
                (task_id,)
            )
            conn.commit()
        return task_id

    @staticmethod
    def pop_task():
        """Attempts to atomically pull and remove a task from the queue header."""
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Grab the oldest task in the line
            cursor.execute("SELECT id, task_name, args FROM task_queue LIMIT 1")
            row = cursor.fetchone()
            if row:
                task_id, task_name, args_json = row
                # Delete it instantly so no other concurrent worker process can steal it
                cursor.execute("DELETE FROM task_queue WHERE id = ?", (task_id,))
                conn.commit()
                return task_id, task_name, json.loads(args_json)
        return None

    @staticmethod
    def write_result(task_id, status, result_val):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE task_results SET status = ?, result = ? WHERE id = ?",
                (status, json.dumps(result_val), task_id)
            )
            conn.commit()

    @staticmethod
    def get_status_payload(task_id):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT status, result FROM task_results WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row:
                return row[0], json.loads(row[1]) if row[1] else None
        return "UNKNOWN", None


class TaskReceipt:
    """Mirrors Celery's AsyncResult. Handed to the client instantly as an execution receipt."""
    def __init__(self, task_id):
        self.task_id = task_id

    def get(self, timeout=10):
        """Blocks the client script until the remote worker writes the result to the DB backend."""
        start = time.time()
        while time.time() - start < timeout:
            status, result = BrokerDB.get_status_payload(self.task_id)
            if status == "SUCCESS":
                return result
            if status == "FAILURE":
                raise RuntimeError(f"Distributed task crashed on remote worker: {result}")
            time.sleep(0.2) # Passive polling interval over the I/O storage boundary
        raise TimeoutError("Distributed task execution timed out.")


# =====================================================================
# SYSTEM APPLICATION REGISTRY (THE TASK CODES)
# =====================================================================

def task_heavy_video_render(resolution, frames):
    # This simulation code will be executed ONLY by the worker process
    time.sleep(3) # Simulate heavy computational execution latency
    return f"Rendered {frames} frames cleanly at {resolution} resolution."


# =====================================================================
# ORCHESTRATION MODES
# =====================================================================

def run_worker():
    print(f"=== CLONE WORKER NODE STARTED (PID: {os.getpid()}) ===")
    print("Listening to broker database file for inbound messages... Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Continuously poll the shared storage file
            job = BrokerDB.pop_task()
            
            if job is None:
                time.sleep(0.5) # Prevent a tight loop from pinning the core when idle
                continue
                
            task_id, task_name, args = job
            print(f"[WORKER] Popped Task '{task_name}' [{task_id}]. Processing...")
            
            try:
                if task_name == "video_render":
                    # Dynamic invocation of the task payload mapping
                    output = task_heavy_video_render(*args)
                    BrokerDB.write_result(task_id, "SUCCESS", output)
                    print(f"  -> [WORKER SUCCESS] Completed Task [{task_id}]. Result logged to backend.")
                else:
                    raise KeyError(f"Unknown task registered: {task_name}")
            except Exception as e:
                BrokerDB.write_result(task_id, "FAILURE", str(e))
                print(f"  -> [WORKER CRASH] Task [{task_id}] failed: {e}")
                
    except KeyboardInterrupt:
        print("\nWorker shutting down cleanly.")

def run_client():
    print(f"=== CLIENT APPLICATION BOOTED (PID: {os.getpid()}) ===")
    
    # Define payload arguments
    task_args = ["4K_UltraHD", 240]
    print(f"[Client UI] User triggered a heavy video export. Offloading to broker...")
    
    start_time = time.time()
    
    # 1. PUSH TO BROKER: Fire-and-forget message serialization
    receipt = TaskReceipt(BrokerDB.push_task("video_render", task_args))
    
    print(f"[Client UI] Task successfully queued! Generated Task ID receipt: {receipt.task_id}")
    print("Main Client Thread is 100% responsive. User can still click around the web interface UI instantly...\n")
    
    # Simulate the client doing other lightweight application loop tasks right away
    for i in range(3):
        print(f"  [Client UI] Animating loading bar step {i+1}...")
        time.sleep(0.5)
        
    print("\n[Client UI] Client now decides to block and wait for the final video file asset...")
    
    # 2. GATHER FROM BACKEND: Block until the remote worker updates the shared state row
    final_video_file = receipt.get()
    
    print(f"\n[Client UI] Received final asset from result backend: '{final_video_file}'")
    print(f"Client lifecycle finalized in {time.time() - start_time:.2f}s total real-world time.")


if __name__ == "__main__":
    BrokerDB.init_db()
    
    # Parse CLI flags to separate worker execution from client execution
    if len(sys.argv) > 1 and sys.argv[1] == "worker":
        run_worker()
    else:
        run_client()