import asyncio
import random
import time

async def log_producer(queue):
    print("[Producer] Initializing log stream generation matrix...")
    
    # Mock data pool with mixed priorities: (Priority Weight, Task Name)
    # Remember: Lower numbers represent higher priority status!
    log_packets = [
        (3, "Low-Priority: Sync user profile image cache"),
        (1, "CRITICAL: Database transaction failure recovery"),
        (3, "Low-Priority: Compress older log blocks"),
        (2, "Medium-Priority: Process automated billing webhook"),
        (1, "CRITICAL: Security firewall breach mitigation")
    ]
    
    for priority, description in log_packets:
        print(f"[Producer] Enqueueing event -> Priority [{priority}] | {description}")
        # Put accepts the tuple and automatically sorts it on the heap
        await queue.put((priority, description))
        await asyncio.sleep(0.1)

async def log_consumer(worker_id, queue):
    print(f"  [Consumer-{worker_id}] Activated and listening for queue frames...")
    try:
        while True:
            # Blocks non-blockingly until an item is available
            priority, description = await queue.get()
            
            print(f"  [Consumer-{worker_id}] ⚙️  Processing -> Priority [{priority}] | Description: {description}")
            # Simulate processing time based on task severity
            processing_window = 0.5 if priority == 1 else 0.2
            await asyncio.sleep(processing_window)
            
            # Register work completion state
            queue.task_done()
            print(f"  [Consumer-{worker_id}] Finished task frame.")
            
    except asyncio.CancelledError:
        print(f"  [Consumer-{worker_id}] Cancellation signal received. Stopping worker.")

async def main():
    print("=== STARTING PRIORITY QUEUE ORCHESTRATION LAYER ===\n")
    start_time = time.time()
    
    # Instantiate the structural Priority Queue
    shared_work_channel = asyncio.PriorityQueue()
    
    # 1. FAN-OUT: Start the Producer and a pool of background Consumers
    producer_task = asyncio.create_task(log_producer(shared_work_channel))
    
    consumer_pool = [
        asyncio.create_task(log_consumer(f"Node-{i}", shared_work_channel))
        for i in range(1, 3)
    ]
    
    # Wait for the producer to finish adding all jobs
    await producer_task
    print("\n[Main] Producer finished data stream injection.")
    
    # 2. FAN-IN: Block main until the queue is completely drained
    print("[Main] Blocking on queue.join() until all tasks reach task_done()...")
    await shared_work_channel.join()
    print("\n[Main] Success! All queue items have been fully verified and cleared.")
    
    # 3. CLEAN UP: Shut down the persistent background consumers
    print("[Main] Tearing down consumer background pool processes...")
    for worker in consumer_pool:
        worker.cancel()
        
    # Let the loop execute the cancellation blocks cleanly
    await asyncio.gather(*consumer_pool, return_exceptions=True)
    print(f"\nExecution loop finalized in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())