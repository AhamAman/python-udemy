import asyncio
import time
import random

async def network_ingest_worker(name, simulated_lag):
    print(f"  [{name}] Network pipe active. Lagging for {simulated_lag}s...")
    await asyncio.sleep(simulated_lag)
    print(f"  [{name}] Finished processing.")
    return f"Data_{name}"

async def main():
    print("=== INITIALIZING CONCURRENT WORK ENGINES ===")
    
    # Define tasks with explicit variable latencies
    # Task Alpha is slow (2s), Task Beta is lightning fast (0.5s)
    tasks_meta = [("Alpha", 2.0), ("Beta", 0.5), ("Gamma", 1.0)]

    # 1. TESTING GATHER (Ordered Aggregation)
    print("\n--- Phase 1: Deploying asyncio.gather ---")
    start = time.time()
    coros = [network_ingest_worker(n, l) for n, l in tasks_meta]
    
    # Fan-Out/Fan-In Checkpoint
    gather_results = await asyncio.gather(*coros)
    print(f"[Gather Output] Unified Array: {gather_results} (Took {time.time() - start:.2f}s)")


    # 2. TESTING AS_COMPLETED (Stream Processing Optimization)
    print("\n--- Phase 2: Deploying asyncio.as_completed ---")
    start = time.time()
    tasks = [asyncio.create_task(network_ingest_worker(n, l)) for n, l in tasks_meta]
    
    print("[As_Completed Output] Consuming iterator stream on the fly:")
    for completed_future in asyncio.as_completed(tasks):
        # Unpacks the next available result dynamically
        result_token = await completed_future
        print(f"  -> Dynamic stream pulled: '{result_token}' at {time.time() - start:.2f}s")


    # 3. TESTING WAIT WITH FIRST_COMPLETED (Race Condition/Timeout Strategy)
    print("\n--- Phase 3: Deploying asyncio.wait (FIRST_COMPLETED) ---")
    start = time.time()
    task_set = {asyncio.create_task(network_ingest_worker(n, l)) for n, l in tasks_meta}
    
    # Wait only until the very first task completes
    done_set, pending_set = await asyncio.wait(task_set, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"\n[Wait Summary Checkpoint at {time.time() - start:.2f}s]")
    print(f"  * Total tasks that reached DONE state: {len(done_set)}")
    for t in done_set:
        print(f"    - Winner Task Result: {t.result()}")
        
    print(f"  * Total tasks left running in PENDING state: {len(pending_set)}")
    
    # Clean up background dangling tasks by cancelling them securely
    print("  * Cleaning up pending task leaks...")
    for t in pending_set:
        t.cancel()

if __name__ == "__main__":
    asyncio.run(main())