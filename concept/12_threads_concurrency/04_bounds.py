import time
import hashlib

def io_bound_task():
    # Simulating a synchronous, blocking network request or file read
    time.sleep(1) 

def cpu_bound_task():
    # Simulating heavy math: generating 5 million secure hashes
    # This keeps the CPU core pinned at 100% processing capacity
    for _ in range(5_000_000):
        hashlib.sha256(b"causality").hexdigest()

if __name__ == "__main__":
    print("=== STARTING PERFORMANCE BENCHMARK ===")
    
    # 1. Measure Synchronous I/O-Bound Work
    start = time.time()
    print("\nRunning 3 I/O-bound tasks sequentially...")
    io_bound_task()
    io_bound_task()
    io_bound_task()
    io_duration = time.time() - start
    print(f"I/O Throughput: 3 tasks completed in {io_duration:.2f} seconds.")
    print("Notice: Your CPU was entirely idle during this wait time.")
    
    # 2. Measure CPU-Bound Work
    start = time.time()
    print("\nRunning 1 CPU-bound math task...")
    cpu_bound_task()
    cpu_duration = time.time() - start
    print(f"CPU Duration: Completed in {cpu_duration:.2f} seconds.")
    print("Notice: Your CPU core was running at maximum capacity here.")