import asyncio
import time

async def persistent_data_streamer():
    print("  [Streamer] Opening cloud data sockets...")
    try:
        for i in range(1, 11):
            print(f"  [Streamer] Streaming data packet batch #{i}...")
            # Each await point checks for scheduled internal CancelledErrors
            await asyncio.sleep(0.5)
            
    except asyncio.CancelledError:
        print("  [Streamer] 🛑 Cancellation signal caught mid-sentence on the heap!")
        print("  [Streamer] Initializing rollback procedures. Flushing unwritten chunks...")
        await asyncio.sleep(0.1) # Simulating a fast async cleanup task
        raise # Re-raising to finalize task closure
        
    finally:
        print("  [Streamer] Clean up sequence complete: Hardware socket channels closed.")

async def main():
    print("=== INITIALIZING SHUTDOWN & CANCELLATION TEST MATRIX ===\n")
    start = time.time()
    
    # Wrap coroutine into a Task frame to boot it concurrently in the background
    stream_task = asyncio.create_task(persistent_data_streamer())
    
    # Let the streamer process for 1.6 seconds (should finish roughly 3 loops)
    await asyncio.sleep(1.6)
    
    print(f"\n[Main] Current Streamer Status: Done? {stream_task.done()}")
    print("[Main] Resource budget limit reached or user hit 'Cancel'. Issuing task.cancel()...")
    
    # Inject CancelledError schedule flag
    stream_task.cancel()
    
    try:
        # Await the task to let it process its exception handling phase completely
        await stream_task
    except asyncio.CancelledError:
        print("[Main] Confirmed: Task raised CancelledError back to caller context.")
        
    print(f"\n[Main] Final State Audit: Done? {stream_task.done()} | Cancelled? {stream_task.cancelled()}")
    print(f"Lifecycle finalized in {time.time() - start:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())