import asyncio
import time
import random

async def secure_network_fetcher(target_id, rate_gate):
    # Acquire a slot from the semaphore guard. 
    # If 3 workers already have slots, this line suspends this worker in the loop's queue.
    async with rate_gate:
        print(f"  [PASSED GATE] [Task-{target_id}] Claimed network slot. Opening connection socket...")
        start_fetch = time.time()
        
        # Simulate a fluctuating live network download
        await asyncio.sleep(random.uniform(1.0, 2.0))
        
        print(f"  [RELEASE]     [Task-{target_id}] Download finished in {time.time() - start_fetch:.2f}s. Dropping slot.")
        # Exiting the async with block automatically releases the token for the next waiting task

async def main():
    print("=== INITIALIZING CONCURRENT THROTTLED RATE LIMITER ===")
    print("Deploying 10 download jobs through a Max-3 Semaphore gate...\n")
    start_time = time.time()
    
    # Establish our concurrency restriction gatekeeper primitive
    concurrency_gate = asyncio.Semaphore(3)
    
    # Fan-Out 10 independent scraping tasks into the loop queue all at once
    scraping_tasks = [
        asyncio.create_task(secure_network_fetcher(i, concurrency_gate)) 
        for i in range(1, 11)
    ]
    
    # Fan-In results aggregation point
    await asyncio.gather(*scraping_tasks)
    
    print(f"\nAll 10 network ingestions successfully completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())