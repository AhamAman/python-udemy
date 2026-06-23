import threading
import queue
import time
import random

# Create a thread-safe FIFO Queue
task_pipeline = queue.Queue(maxsize=5)

def worker_thread(worker_id):
    while True:
        try:
            # 1. GET: Pull an item. If empty, the thread automatically blocks here.
            # timeout=3 allows the thread to gracefully exit if the queue stays empty at the end
            task = task_pipeline.get(timeout=3)
            
            print(f"  [Worker-{worker_id}] Processing: {task}")
            # Simulate variable task execution time
            time.sleep(random.uniform(0.5, 1.2))
            
            print(f"  [Worker-{worker_id}] Finished: {task}")
            
            # 2. TASK_DONE: Signal the queue that this item is fully resolved
            task_pipeline.task_done()
            
        except queue.Empty:
            # If no tasks arrive within the timeout window, exit the loop
            print(f"  [Worker-{worker_id}] No tasks left. Shutting down.")
            break

if __name__ == "__main__":
    print("=== INITIALIZING WORK DISTRIBUTION POOL ===")
    
    # Spawn 3 worker threads
    num_workers = 3
    for i in range(1, num_workers + 1):
        t = threading.Thread(target=worker_thread, args=(i,), daemon=True)
        t.start()

    print(f"Created {num_workers} background worker threads waiting for work...\n")
    time.sleep(1)

    # Main thread acts as the Producer, loading work into the pipeline
    tasks = ["Download-Image", "Parse-JSON", "Update-DB", "Generate-Report", "Send-Email"]
    
    print("[Main Thread] Dispensing 5 tasks into the shared queue...")
    for task in tasks:
        task_pipeline.put(task)
    
    print("[Main Thread] All tasks queued. Waiting for worker pool execution to finish...")
    
    # 3. JOIN: Block the main thread until every task has sent a task_done() signal
    task_pipeline.join()
    
    print("\n=== PIPELINE PROCESSED. ALL TASKS COMPLETED. ===")