import asyncio

async def network_stream_worker(name, delay, should_crash=False):
    print(f"  [{name}] Stream connection initialized...")
    await asyncio.sleep(delay)
    
    if should_crash:
        print(f"  [{name}] 🔴 Hardware transceiver failure!")
        raise ConnectionResetError("Remote server abruptly closed socket.")
        
    print(f"  [{name}] ✨ Stream processing complete.")
    return f"{name}_Finished_Payload"

async def main():
    print("=== BOOTING RECONNAISSANCE MONITORING MATRIX ===\n")
    
    # Schedule three unique tasks with different profiles
    task_good  = asyncio.create_task(network_stream_worker("Task-Good", 1.0))
    task_slow  = asyncio.create_task(network_stream_worker("Task-Slow", 4.0))
    task_fault = asyncio.create_task(network_stream_worker("Task-Faulty", 1.5, should_crash=True))
    
    all_tasks = [task_good, task_slow, task_fault]
    
    # 1. Active Polling Audit
    print("[Monitor] Checking initial state matrix...")
    await asyncio.sleep(0.5)
    for t in all_tasks:
        print(f"   -> Audit check: {t.get_name()} | Done? {t.done()}")
        
    # Wait until the faulty task and good task resolve/crash
    print("\n[Monitor] Waiting for mid-lifecycle completions...")
    await asyncio.sleep(1.5)
    
    # 2. Enforcement Action: Cancel the slow task because it exceeds our resource budget
    print(f"\n[Monitor] Task-Slow is taking too long. Issuing cancellation command...")
    task_slow.cancel()
    
    # Give the loop one final tick to process the cancellation and crashes
    await asyncio.sleep(0.1)
    
    print("\n================ SYSTEM STATUS AUDIT REPORT ================")
    for t in all_tasks:
        name = t.get_name()
        if t.cancelled():
            print(f"  * {name} -> 🚫 STATE: CANCELLED")
        elif t.done():
            # Extract exception if it exists without re-raising it
            err = t.exception()
            if err:
                print(f"  * {name} -> 💥 STATE: CRASHED | Error Captured: {err}")
            else:
                print(f"  * {name} -> ✅ STATE: SUCCESS | Result: {t.result()}")

if __name__ == "__main__":
    asyncio.run(main())