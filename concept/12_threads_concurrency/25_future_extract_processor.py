import time
import random
from concurrent.futures import ThreadPoolExecutor

def erratic_worker(task_id):
    print(f"  [Pool Worker] Starting Task-{task_id}...")
    time.sleep(random.uniform(0.6, 1.2))
    
    # Intentionally trigger an error frame to demonstrate safe exception trapping
    if task_id == 3:
        raise ValueError("Critical engineering failure inside Task-3!")
        
    return f"Result-Payload-From-Task-{task_id}"

if __name__ == "__main__":
    print("=== DEPLOYING THREAD POOL EXECUTOR (Max 2 Workers) ===")
    
    # 1. EXECUTOR SUBMIT & FUTURE LIFECYCLE
    # Context manager automatically handles calling shutdown() at the end block
    with ThreadPoolExecutor(max_workers=2) as executor:
        print("\n--- Phase 1: Tracking Individual Futures via .submit() ---")
        
        # Dispatch tasks. The main loop does not freeze.
        future_2 = executor.submit(erratic_worker, task_id=2)
        future_3 = executor.submit(erratic_worker, task_id=3) # Will throw error
        
        print(f"Immediate Future-2 State right after submission: Running={future_2.running()}")
        
        # Safely block and extract values using the Future boundary interface
        print(f"Extracting Future-2 Result: {future_2.result()}")
        
        print("\nExtracting Future-3 (The Faulted Task)...")
        try:
            # The exception that happened on the background worker thread 
            # is automatically marshaled and raised here inside the Main Thread
            data = future_3.result()
        except ValueError as err:
            print(f"-> Safely trapped worker crash inside Main Thread: {err}")

    # 2. EXECUTOR MAP (Clean Data Processing Pipelines)
    with ThreadPoolExecutor(max_workers=3) as pool:
        print("\n--- Phase 2: High Volume Data Processing via .map() ---")
        task_inputs = [10, 20, 30, 40]
        
        def simple_multiplier(x):
            time.sleep(0.4)
            return x * 10
            
        print(f"Mapping task batches {task_inputs} uniformly across worker matrix...")
        start = time.time()
        
        # .map handles queue tracking and worker dispatch under the hood implicitly
        results_iterator = pool.map(simple_multiplier, task_inputs)
        
        # Unpack results iterator
        final_list = list(results_iterator)
        print(f"Gathered ordered output mapping: {final_list}")
        print(f"Map operations concluded concurrently in {time.time() - start:.2f}s")