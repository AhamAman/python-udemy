import time
import threading
import asyncio

TASKS_COUNT = 1000
IO_DELAY = 1.0

# =====================================================================
# 1. SYNCHRONOUS BLOCKING (The Line-by-Line Bottleneck)
# =====================================================================
def sync_worker(task_id):
    # time.sleep() forces the entire OS thread to freeze and block
    time.sleep(IO_DELAY)

def run_synchronous_demo():
    print(f"[Sync] Sequentially processing {TASKS_COUNT} blocking tasks...")
    start = time.time()
    
    for i in range(TASKS_COUNT):
        sync_worker(i)
        
    duration = time.time() - start
    print(f"❌ Synchronous Total Time: {duration:.2f} seconds\n")


# =====================================================================
# 2. MULTI-THREADED PREEMPTION (The High Resource Approach)
# =====================================================================
def run_threaded_demo():
    print(f"[Threads] Spawning {TASKS_COUNT} OS threads simultaneously...")
    start = time.time()
    
    threads = []
    for i in range(TASKS_COUNT):
        t = threading.Thread(target=sync_worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    duration = time.time() - start
    print(f"✅ Threaded Total Time: {duration:.2f} seconds")
    print(f"👉 Note: The OS kernel had to context-switch {TASKS_COUNT} heavy thread stacks.\n")


# =====================================================================
# 3. ASYNCHRONOUS COOPERATIVE (The Single-Threaded Event Loop)
# =====================================================================
async def async_worker(task_id):
    # 'await' is our cooperative yield token. 
    # asyncio.sleep() registers a non-blocking timer and yields control back to the loop.
    await asyncio.sleep(IO_DELAY)

async def run_async_demo():
    print(f"[Async] Interleaving {TASKS_COUNT} cooperative tasks on ONE thread...")
    start = time.time()
    
    # Package all 1,000 tasks as coroutines
    tasks = [async_worker(i) for i in range(TASKS_COUNT)]
    
    # Gather them onto the single-threaded Event Loop engine
    await asyncio.gather(*tasks)
    
    duration = time.time() - start
    print(f"⚡ Async Total Time: {duration:.2f} seconds")
    print("👉 Note: Executed entirely on a single thread with ZERO kernel context switches.")


if __name__ == "__main__":
    print("=== BEGINNING CONCURRENCY PARADIGM BENCHMARK ===")
    
    # 1. Run Sync (We will only run 3 tasks because 1,000 would take 1,000 seconds!)
    original_count = TASKS_COUNT
    TASKS_COUNT = 3
    run_synchronous_demo()
    
    # Restore count for concurrent models
    TASKS_COUNT = original_count
    
    # 2. Run Multi-Threaded
    run_threaded_demo()
    
    # 3. Run Asynchronous Event Loop
    asyncio.run(run_async_demo())