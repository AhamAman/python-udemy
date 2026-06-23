import asyncio
import time

# Shared memory target
shared_database_counter = 0

async def unprotected_increment_worker(worker_id):
    global shared_database_counter
    
    # Read state
    local_read = shared_database_counter
    
    # SIMULATED NETWORK I/O: Force a suspension point mid-transaction
    await asyncio.sleep(0.001)
    
    # Write state
    shared_database_counter = local_read + 1


async def protected_increment_worker(worker_id, system_lock):
    global shared_database_counter
    
    # Acquire exclusive passage across all internal await points
    async with system_lock:
        local_read = shared_database_counter
        
        # Sibling tasks cannot enter this block while this sleep resolves
        await asyncio.sleep(0.001)
        
        shared_database_counter = local_read + 1

async def main():
    global shared_database_counter
    
    # --- PHASE 1: UNPROTECTED RACE CONDITION ---
    print("=== RUNNING RUNTIME UNPROTECTED CONCURRENT MODIFICATION ===")
    shared_database_counter = 0
    
    # Fan-Out 100 workers attempting to increment the counter
    tasks = [asyncio.create_task(unprotected_increment_worker(i)) for i in range(100)]
    await asyncio.gather(*tasks)
    
    print(f" Expected Counter Value: 100")
    print(f" Actual Counter Value:   {shared_database_counter}")
    print(" 👉 Result: State was corrupted because tasks interleaved across suspension points.\n")


    # --- PHASE 2: PROTECTED MUTEX MUTATION ---
    print("=== RUNNING PROTECTED MUTEX MODIFICATION ===")
    shared_database_counter = 0
    cluster_lock = asyncio.Lock()
    
    protected_tasks = [
        asyncio.create_task(protected_increment_worker(i, cluster_lock)) 
        for i in range(100)
    ]
    await asyncio.gather(*protected_tasks)
    
    print(f" Expected Counter Value: 100")
    print(f" Actual Counter Value:   {shared_database_counter}")
    print(" ✅ Result: Lock serialization guaranteed deterministic accuracy!")

if __name__ == "__main__":
    asyncio.run(main())