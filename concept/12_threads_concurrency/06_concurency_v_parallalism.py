import time
import asyncio
from multiprocessing import Process

# A CPU-bound math task that takes physical processing time
def cpu_math_task(task_id):
    start = time.time()
    count = 0
    for i in range(15_000_000):
        count += i
    print(f"  [Core Work] Task {task_id} completed in {time.time() - start:.2f}s")

# An Async task simulating concurrent I/O waiting
async def async_io_task(task_id):
    start = time.time()
    await asyncio.sleep(1) # Yields control while waiting
    print(f"  [Async I/O] Task {task_id} woke up after {time.time() - start:.2f}s")

async def run_concurrency():
    # Concurrency: 3 tasks running on ONE thread, interleaving their idle time
    await asyncio.gather(async_io_task(1), async_io_task(2), async_io_task(3))

if __name__ == "__main__":
    print("==================================================")
    print("      DEMONSTRATING ARCHITECTURAL MECHANICS       ")
    print("==================================================")

    # 1. SEQUENTIAL (Baseline)
    print("\n1. Running Tasks Sequentially...")
    start = time.time()
    cpu_math_task(1)
    cpu_math_task(2)
    seq_duration = time.time() - start
    print(f"-> Sequential Total Time: {seq_duration:.2f} seconds")

    # 2. CONCURRENCY (Interleaved on a single thread)
    print("\n2. Running Tasks Concurrently (Single Thread Async)...")
    start = time.time()
    asyncio.run(run_concurrency())
    con_duration = time.time() - start
    print(f"-> Concurrent Total Time: {con_duration:.2f} seconds")
    print("   Notice: 3 tasks took ~1 second total because they shared the wait time!")

    # 3. PARALLELISM (True simultaneous multi-core execution)
    print("\n3. Running Tasks In Parallel (Multiple CPU Cores)...")
    start = time.time()
    
    p1 = Process(target=cpu_math_task, args=(1,))
    p2 = Process(target=cpu_math_task, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    par_duration = time.time() - start
    print(f"-> Parallel Total Time: {par_duration:.2f} seconds")
    print(f"   Notice: Compare this to the Sequential time. Two cores did the math together.")