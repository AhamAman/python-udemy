import threading
import queue
import time
import random

# PriorityQueue sorts items based on the first element of a tuple: (priority_number, data)
# LOWEST numbers are pulled out FIRST (0 = Highest Priority)
job_queue = queue.PriorityQueue()

def job_processor(worker_id):
    while True:
        priority, job_name = job_queue.get()
        
        if job_name == "SHUTDOWN":
            job_queue.task_done()
            break
            
        print(f"  [Worker-{worker_id}] Executing [Priority {priority}] Task: {job_name}")
        time.sleep(random.uniform(0.4, 0.8))
        job_queue.task_done()

if __name__ == "__main__":
    print("=== INITIALIZING PRIORITY JOB QUEUE ===")
    
    # Push tasks out of chronological order to test sorting
    print("Loading tasks into queue out of order...")
    job_queue.put((3, "Low-Priority: Sync User Avatars"))
    job_queue.put((1, "High-Priority: Process Payment Transaction"))
    job_queue.put((0, "CRITICAL: Kernel Out-of-Memory Alert"))
    job_queue.put((2, "Medium-Priority: Generate Monthly Analytics Report"))
    
    # Spin up two concurrent worker threads
    workers = [threading.Thread(target=job_processor, args=(i,), daemon=True) for i in range(1, 3)]
    for w in workers:
        w.start()
        
    # Wait for all current jobs to finish processing
    job_queue.join()
    
    # Clean shutdown
    for _ in workers:
        job_queue.put((99, "SHUTDOWN"))
    for w in workers:
        w.join()
        
    print("=== ALL PRIORITIZED JOBS PROCESSED ===")