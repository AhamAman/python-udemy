import asyncio
import time
import requests

def blocking_demo():
    print("\n--- Starting Blocking Demo ---")
    start = time.time()
    
    # This network request BLOCKS the thread. Nothing else can happen here.
    print("Sending request 1 (Blocking)...")
    res1 = requests.get("https://httpbin.org/delay/2") 
    
    print("Sending request 2 (Blocking)...")
    res2 = requests.get("https://httpbin.org/delay/2")
    
    print(f"Blocking execution finished in {time.time() - start:.2f} seconds.")

async def async_worker(task_id):
    print(f"Sending request {task_id} (Non-Blocking)...")
    # Using an async library simulates non-blocking I/O 
    # The 'await' keyword yields control back to the event loop while waiting
    await asyncio.sleep(2) 
    print(f"Request {task_id} completed!")

async def non_blocking_demo():
    print("\n--- Starting Non-Blocking Demo ---")
    start = time.time()
    
    # Fire off both tasks concurrently without waiting for the first to finish
    await asyncio.gather(
        async_worker(1),
        async_worker(2)
    )
    print(f"Non-Blocking execution finished in {time.time() - start:.2f} seconds.")

if __name__ == "__main__":
    # 1. Shows that blocking forces tasks to run strictly sequentially (2s + 2s = 4s)
    blocking_demo()
    
    # 2. Shows that non-blocking allows tasks to overlap in time, completing together (~2s total)
    asyncio.run(non_blocking_demo())