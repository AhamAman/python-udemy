import threading
import queue
import time
import random

class WorkerPool:
    def __init__(self, num_threads):
        self.task_queue = queue.Queue()
        self.workers = []
        
        # Pre-spawn permanent worker threads
        for i in range(num_threads):
            t = threading.Thread(target=self._worker_loop, args=(i+1,), daemon=True)
            self.workers.append(t)
            t.start()
            
    def _worker_loop(self, worker_id):
        while True:
            # Grab a task. The task payload is an executable function/closure
            func, args, kwargs = self.task_queue.get()
            
            # Check for poison pill to shut down this specific thread
            if func is None:
                self.task_queue.task_done()
                break
                
            try:
                # Execute the arbitrary workload function
                func(worker_id, *args, **kwargs)
            except Exception as e:
                print(f"Worker-{worker_id} encountered an exception: {e}")
                
            self.task_queue.task_done()
        print(f"  [Pool-Thread-{worker_id}] Exited cleanly.")

    def submit(self, func, *args, **kwargs):
        # Package the execution frame and queue it
        self.task_queue.put((func, args, kwargs))

    def wait_for_completion(self):
        # Block until all queued jobs send task_done()
        self.task_queue.join()

    def shutdown(self):
        # Dispense a poison pill for every thread in the pool
        for _ in self.workers:
            self.task_queue.put((None, None, None))
        for t in self.workers:
            t.join()

# Target task to run inside our pool
def complex_math_job(worker_id, job_name, compute_delay):
    print(f"  [Worker-{worker_id}] Processing {job_name}...")
    time.sleep(compute_delay)
    print(f"  [Worker-{worker_id}] Completed {job_name}.")

if __name__ == "__main__":
    print("=== INITIALIZING WORKER POOL (3 THREADS) ===")
    pool = WorkerPool(num_threads=3)
    
    # Submit 6 jobs to a pool of only 3 threads
    for i in range(1, 7):
        pool.submit(complex_math_job, f"Job-ID-{i}", random.uniform(0.5, 1.2))
        
    print("All jobs submitted. Pool is executing workloads asynchronously...\n")
    pool.wait_for_completion()
    
    print("\nShutting down pool...")
    pool.shutdown()
    print("=== SYSTEM DOWN ===")