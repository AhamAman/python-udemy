import asyncio
import time
import random

async def database_query_worker(worker_id):
    # Simulate variable network response lag between 0.5 and 1.5 seconds
    simulated_latency = random.uniform(0.5, 1.5)
    print(f"  [Worker-{worker_id}] Query started. Estimated lag: {simulated_latency:.2f}s")
    
    await asyncio.sleep(simulated_latency)
    
    print(f"  [Worker-{worker_id}] Query finished and compiled.")
    return f"Data_Row_{worker_id}"

async def main():
    print("=== INITIALIZING MULTI-TASK DISTRIBUTED EXECUTION ===")
    start_time = time.time()
    
    # 1. SPARK PHASE: Generate 5 background tasks concurrently using create_task
    # This populates the Event Loop's Ready Queue instantly
    task_batch = [asyncio.create_task(database_query_worker(i)) for i in range(1, 6)]
    
    print(f"[Main Loop] Spawned {len(task_batch)} concurrent database queries. Gathering results...\n")
    
    # 2. GATHER PHASE: Block main until ALL tasks in the batch reach the DONE state
    # asyncio.gather unpacks the task list and returns their results in order
    compiled_results = await asyncio.gather(*task_batch)
    
    print("\n=== DATA EXTRACTION COMPLETE ===")
    print(f"Aggregated Payload Matrix: {compiled_results}")
    print(f"Total Concurrent Timeline: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())