import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def heavy_cpu_crunch(n):
    # Pure CPU-bound calculation loop
    count = 0
    for i in range(20_000_000):
        count += i + n
    return count

if __name__ == "__main__":
    task_inputs = [1, 2, 3, 4]
    print(f"=== BENCHMARKING COMPUTATION VS THE PYTHON GIL ===")
    print(f"Distributing 4 heavy calculation blocks across cores...\n")

    # 1. TEST MULTI-THREADING (Stuck under the GIL single-core bottleneck)
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(heavy_cpu_crunch, task_inputs))
    thread_duration = time.time() - start
    print(f"-> ThreadPoolExecutor Total Time: {thread_duration:.4f} seconds")

    # 2. TEST MULTI-PROCESSING (True hardware parallelism bypasses the GIL)
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(heavy_cpu_crunch, task_inputs))
    process_duration = time.time() - start
    print(f"-> ProcessPoolExecutor Total Time: {process_duration:.4f} seconds")
    
    print(f"\nHardware Efficiency Gain: Process execution was {thread_duration / process_duration:.2f}x faster!")