import asyncio
import time

async def intensive_network_job(job_id, delay):
    print(f"  [Job-{job_id}] Execution started inside the loop...")
    # Task shifts to SUSPENDED here, letting other tasks run
    await asyncio.sleep(delay)
    print(f"  [Job-{job_id}] Execution completed!")
    return f"Result-Data-{job_id}"

async def main():
    print("=== INITIALIZING ASYNCIO TASK MANAGEMENT PLATFORM ===\n")
    start_time = time.time()

    # 1. Spawn Task 1 (Schedules it to run in the background)
    print("[Main] Creating Task 1...")
    task1 = asyncio.create_task(intensive_network_job("Alpha", 2.0))
    print(f"   -> Task 1 Initial State Check: done() = {task1.done()}") # Expected: False

    # 2. Spawn Task 2 (Schedules it to run simultaneously)
    print("\n[Main] Creating Task 2...")
    task2 = asyncio.create_task(intensive_network_job("Beta", 1.0))
    
    print("\n[Main] Both tasks are now queued. Main thread is completely free to execute local logic...")
    # Demonstrate non-blocking nature by running a quick local compute loop
    for i in range(3):
        print(f"  [Main UI Thread] Processing local animation frame {i+1}...")
        await asyncio.sleep(0.2)

    print(f"\n[Main] Time elapsed so far: {time.time() - start_time:.2f}s")
    print(f"   -> Task 2 Status Check before awaiting: done() = {task2.done()}")

    print("\n[Main] Now blocking main to wait for Task 1's final result...")
    # Unpack the result. This blocks the main coroutine until Task 1 hits the DONE state.
    result1 = await task1
    
    # Task 2 only took 1.0s, so it must be done by now since Task 1 took 2.0s
    result2 = await task2 
    
    print(f"\n[Main] Extraction Complete!")
    print(f"   -> Task 1 Result: {result1} | Status: done() = {task1.done()}")
    print(f"   -> Task 2 Result: {result2} | Status: done() = {task2.done()}")
    print(f"\nTotal System Processing Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())