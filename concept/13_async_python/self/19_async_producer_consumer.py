import asyncio
import random
import time

async def task_producer(work_queue):
    print("[Producer] Starting item discovery scan...")
    for i in range(1, 6):
        item_payload = f"Scraped_Data_Token_{i}"
        
        # put() is an active suspension point if the queue hits its maxsize limit
        print(f"[Producer] Attempting to queue item {i} (Current Queue Size: {work_queue.qsize()})")
        await work_queue.put(item_payload)
        print(f"[Producer] Successfully added item {i} to the channel.")
        
        # Simulate variable speed discovery
        await asyncio.sleep(random.uniform(0.1, 0.3))
        
    print("[Producer] Discovery finished. Placing exit signals for consumers.")
    # Place None tokens as explicit termination traps (poison pills) for our 3 workers
    for _ in range(3):
        await work_queue.put(None)

async def task_consumer(worker_name, work_queue):
    print(f"  [{worker_name}] Worker spawned and listening...")
    while True:
        # get() blocks non-blockingly if the queue is empty
        payload = await work_queue.get()
        
        # Check for poison pill termination flag
        if payload is None:
            work_queue.task_done()
            print(f"  [{worker_name}] Received exit signal. Powering down worker thread context.")
            break
            
        print(f"  [{worker_name}] Processing item: '{payload}'")
        # Simulate heavy document parsing/processing delay
        await asyncio.sleep(random.uniform(0.6, 1.2))
        
        # Tell the queue that this work frame is finalized
        work_queue.task_done()

async def main():
    print("=== STARTING BOUNDED PRODUCER-CONSUMER WORKSTREAM ===")
    start_time = time.time()
    
    # Initialize a bounded queue to enforce strict memory safety boundaries
    shared_pipeline = asyncio.Queue(maxsize=3)
    
    # Fan-Out our workers
    producer_task = asyncio.create_task(task_producer(shared_pipeline))
    consumers = [
        asyncio.create_task(task_consumer(f"Consumer-{name}", shared_pipeline))
        for name in ["Alpha", "Beta", "Gamma"]
    ]
    
    # Gather execution resolution blocks
    await asyncio.gather(producer_task, *consumers)
    print(f"\nPipeline completely drained in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())