import asyncio
import time

async def fetch_database_shard(shard_id, latency):
    print(f"  [Shard-{shard_id}] Query dispatched. Awaiting read for {latency}s...")
    await asyncio.sleep(latency)
    print(f"  [Shard-{shard_id}] Matrix rows extracted successfully.")
    return f"Data_Shard_{shard_id}"

async def main():
    print("=== INITIALIZING HUNG TASK PREVENTION MATRIX ===\n")

    # 1. THE CUMULATIVE CONTEXT MANAGER (asyncio.timeout)
    # Total time budget allocated for BOTH sequential shards combined is 2.5 seconds
    total_budget = 2.5
    print(f"[Policy] Establishing unified context timeout safety fence: {total_budget}s")
    
    start_clock = time.time()
    try:
        async with asyncio.timeout(total_budget):
            # Step A takes 1.0 second (Leaves 1.5 seconds remaining on the clock)
            res_a = await fetch_database_shard("Alpha", 1.0)
            
            # Step B takes 2.0 seconds -> This will exceed the remaining 1.5s window!
            res_b = await fetch_database_shard("Beta", 2.0)
            
            print(f"[Success] Both metrics compiled: {res_a}, {res_b}")
            
    except asyncio.TimeoutError:
        print(f" 🚨 [TIMEOUT] Unified context manager tripped at {time.time() - start_clock:.2f}s!")
        print("    -> Action: Hung task killed. Block terminated downstream leaks.")


    print("\n-------------------------------------------------------------")
    # 2. THE SINGLE ATOMIC WRAPPER (asyncio.wait_for)
    print("[Policy] Testing standalone functional wrapper fence (1.5s budget)...")
    try:
        # Atomic envelope around a single coroutine query
        single_result = await asyncio.wait_for(fetch_database_shard("Gamma", 3.0), timeout=1.5)
        print(f"[Success] Standalone output: {single_result}")
    except asyncio.TimeoutError:
        print(" 🚨 [TIMEOUT] asyncio.wait_for cut off the individual Gamma pipeline.")

if __name__ == "__main__":
    asyncio.run(main())