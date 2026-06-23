import asyncio
import time

async def uncooperative_task():
    print("[Task-Uncooperative] Booted. Running a heavy compute loop for 2 seconds...")
    start = time.time()
    
    # Simulating a bad actor: heavy calculations or synchronous blocking without an 'await'
    while time.time() - start < 2.0:
        pass # Pinned to the CPU core register loop
        
    print("[Task-Uncooperative] Finished processing. Yielding control now.")
    await asyncio.sleep(0.0) # Voluntary yield point

async def cooperative_task(task_id):
    for i in range(3):
        print(f"  [Task-Cooperative-{task_id}] Step {i+1} executed.")
        # Every time this hits await, it yields the thread back to the loop engine
        await asyncio.sleep(0.4)

async def main():
    print("=== STARTING COOPERATIVE SCHEDULING SIMULATION ===\n")
    
    print("[Main] Registering cooperative tasks into the queue...")
    task1 = asyncio.create_task(cooperative_task(1))
    task2 = asyncio.create_task(cooperative_task(2))
    
    # Give them a brief window to interleave their first steps
    await asyncio.sleep(0.1)
    
    print("\n[Main] Registering the uncooperative task block...")
    task3 = asyncio.create_task(uncooperative_task())
    
    # Gather and run all tasks concurrently
    await asyncio.gather(task1, task2, task3)
    print("\n=== SIMULATION COMPLETION MATRIX CLOSED ===")

if __name__ == "__main__":
    asyncio.run(main())