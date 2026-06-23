import asyncio
import time

async def analytics_generation_loop():
    print("  [Worker] Allocated local matrix memory arrays. Processing chunks...")
    try:
        for step in range(1, 101):
            # Simulated chunk processing step
            await asyncio.sleep(0.1)
            if step % 10 == 0:
                print(f"  [Worker] Compiled database aggregation matrix: {step}% complete...")
                
    except asyncio.CancelledError:
        print("  [Worker] 🛑 Intercepted cancellation request! Cleaning up heap arrays...")
        # Clean up database resources or discard open mutations here
        raise
    finally:
        print("  [Worker] Memory buffer flushed. Execution slot released cleanly.")

async def main():
    print("=== STARTING USER SESSION TRANSACTION MANAGER ===")
    start_time = time.time()
    
    # Fan-Out the long running operation to the background
    worker_task = asyncio.create_task(analytics_generation_loop())
    
    # Simulate the user browsing the dashboard for 0.45 seconds before clicking "Log Out"
    await asyncio.sleep(0.45)
    
    print(f"\n[User Event] User explicitly logged out. Killing orphan background tasks...")
    worker_task.cancel()
    
    # Give the task space to bubble up its CancelledError and run its cleanup blocks
    try:
        await worker_task
    except asyncio.CancelledError:
        print("[Main] Verified: Task was safely terminated before polluting global state.")
        
    print(f"\nSystem Runtime Safety Verified in {time.time() - start_time:.2f}s.")

if __name__ == "__main__":
    asyncio.run(main())