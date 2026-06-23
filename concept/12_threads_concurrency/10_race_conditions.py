import threading
import time

# A shared global variable on the Heap
shared_counter = 0
ITERATIONS = 1_000_000

def increment_worker():
    global shared_counter
    for _ in range(ITERATIONS):
        # This looks like 1 step, but under the hood it is 3 CPU steps:
        # 1. Read shared_counter
        # 2. Add 1
        # 3. Write shared_counter
        shared_counter += 1

if __name__ == "__main__":
    print("=== STARTING SHARED MEMORY EXPERIMENT ===")
    print(f"Initial Counter Value: {shared_counter}")
    print(f"Spawning 2 threads. Each will increment the counter {ITERATIONS:,} times.")
    print("Expected mathematical total should be: 2,000,000\n")

    # Create two threads targeting the same global variable
    t1 = threading.Thread(target=increment_worker)
    t2 = threading.Thread(target=increment_worker)

    start_time = time.time()
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("--- Results ---")
    print(f"Actual Final Counter Value: {shared_counter:,}")
    print(f"Lost Updates (Deficit):       {2_000_000 - shared_counter:,}")
    print(f"Execution Time:               {time.time() - start_time:.4f} seconds")