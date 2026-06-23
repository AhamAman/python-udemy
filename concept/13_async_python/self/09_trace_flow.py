import asyncio
import time

async def compute_metrics_worker(node_id):
    # 1. Thread enters this block sequentially
    print(f"  [Time: {time.time() - base_time:.2f}s] [Worker-{node_id}] STEP A: Initiating heavy calculation check...")
    
    # 2. SUSPENSION POINT: The task voluntarily freezes and yields control
    await asyncio.sleep(1.0)
    
    # 5. Thread returns here only after the event loop wakes it up from the ready queue
    print(f"  [Time: {time.time() - base_time:.2f}s] [Worker-{node_id}] STEP B: Resumed! Finalizing data write.")

async def main():
    global base_time
    base_time = time.time()
    print("=== BEGINNING EXECUTION FLOW TRACE ===\n")
    
    # Package two instances of our coroutine into Tasks (places them in the Ready Queue)
    task_one = asyncio.create_task(compute_metrics_worker("Alpha"))
    task_two = asyncio.create_task(compute_metrics_worker("Beta"))
    
    print(f"[Main Loop] Tasks registered. Yielding main control block...")
    # Block main until both background tasks resolve
    await asyncio.gather(task_one, task_two)
    
    print("\n=== TRACE LIFECYCLE CLOSED ===")

if __name__ == "__main__":
    asyncio.run(main())