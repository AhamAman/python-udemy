import asyncio
import time
import random

async def persistent_pool_worker(worker_id, job_queue):
    """A long-running, reusable processing node."""
    print(f"  [Worker-{worker_id}] Node booted and attached to queue pipeline.")
    try:
        while True:
            # Workers block non-blockingly here waiting for incoming job tokens
            job_meta = await job_queue.get()
            
            job_id, compute_weight = job_meta
            print(f"  [Worker-{worker_id}] ⚙️  Processing Job #{job_id} (Complexity Weight: {compute_weight})")
            
            # Simulate processing an intensive network/disk task
            await asyncio.sleep(compute_weight)
            
            print(f"  [Worker-{worker_id}] ✅ Completed Job #{job_id}")
            job_queue.task_done()
            
    except asyncio.CancelledError:
        print(f"  [Worker-{worker_id}] ⛔ Worker pulled from cluster matrix. Shutting down cleanly.")

async def main():
    print("=== INITIALIZING FIXED-SIZE ASYNC WORKER POOL ===")
    start_time = time.time()
    
    # 1. SETUP PHASE: Initialize the communication grid
    job_pipeline = asyncio.Queue()
    NUM_WORKERS = 3
    
    # Spawn a fixed-size cluster matrix of persistent background workers
    worker_nodes = [
        asyncio.create_task(persistent_pool_worker(f"Node-{i}", job_pipeline))
        for i in range(1, NUM_WORKERS + 1)
    ]
    
    # 2. SEED PHASE: Inject a heavy batch of 10 tasks into the pool
    print(f"\n[Main] Populating job queue with workloads...")
    for job_num in range(1, 11):
        simulated_weight = random.uniform(0.2, 0.8)
        await job_pipeline.put((job_num, simulated_weight))
        
    print(f"[Main] All jobs queued. Current pipeline length: {job_pipeline.qsize()}")
    
    # 3. COORDINATION PHASE: Block until all jobs hit task_done()
    print("[Main] Holding thread baseline open until queue is fully drained...\n")
    await job_pipeline.join()
    
    # 4. TEARDOWN PHASE: Safely decommission the background worker fleet
    print("\n[Main] Queue drained. Decommissioning reusable worker pool nodes...")
    for node in worker_nodes:
        node.cancel()
        
    # Let the event loop process the worker cancellation cleanups
    await asyncio.gather(*worker_nodes, return_exceptions=True)
    print(f"\nPipeline processing pool finalized in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())