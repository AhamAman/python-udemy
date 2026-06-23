import asyncio
import time

async def volatile_network_job(job_name, latency, should_fail=False):
    """Simulates a highly volatile backend request."""
    print(f"    [Task-Engine] Executing '{job_name}'...")
    await asyncio.sleep(latency)
    
    if should_fail:
        raise ConnectionRefusedError(f"Remote storage target blocked '{job_name}' connection socket.")
        
    return f"Success_Data_From_{job_name}"

async def core_processor_node(queue, telemetry_ledger):
    """Defensive task wrapper equipped with timeout and crash barriers."""
    while True:
        job_config = await queue.get()
        job_name, latency, force_crash = job_config
        
        # Enforce a strict defensive execution budget per task of 1.5 seconds
        TIMEOUT_BUDGET = 1.5
        
        try:
            # Wrap the volatile operation inside a timeout barrier
            async with asyncio.timeout(TIMEOUT_BUDGET):
                result = await volatile_network_job(job_name, latency, force_crash)
                telemetry_ledger["SUCCEEDED"].append((job_name, result))
                print(f"  [SYSTEM MONITOR] ✅ Task '{job_name}' resolved cleanly.")
                
        except asyncio.TimeoutError:
            # Catch timeouts, prevent hung task leak, and log telemetry
            telemetry_ledger["TIMED_OUT"].append(job_name)
            print(f"  [SYSTEM MONITOR] 🚨 HUNG TASK ENFORCED: Task '{job_name}' exceeded execution budget limit of {TIMEOUT_BUDGET}s. Killed.")
            
        except Exception as err:
            # Catch internal application crashes cleanly without breaking the node loop
            telemetry_ledger["FAILED"].append((job_name, str(err)))
            print(f"  [SYSTEM MONITOR] 💥 CRASH ISOLATED: Task '{job_name}' failed with error: {err}")
            
        finally:
            queue.task_done()

async def main():
    print("=== INITIALIZING FAULT-TOLERANT TASK PROCESSING ENGINE ===\n")
    start_time = time.time()
    
    # Establish shared state tracking ledger and input queue channel
    job_queue = asyncio.Queue()
    system_telemetry = {"SUCCEEDED": [], "TIMED_OUT": [], "FAILED": []}
    
    # Initialize 5 specific jobs showcasing different edge-case profiles
    workload_batch = [
        ("Job-Alpha", 0.4, False), # Should succeed cleanly
        ("Job-Beta",  2.5, False), # Should trigger a TIMEOUT (Takes 2.5s > 1.5s budget)
        ("Job-Gamma", 0.2, True),  # Should trigger an ISOLATED CRASH (Throws a direct Error)
        ("Job-Delta", 0.5, False), # Should succeed cleanly
    ]
    
    for job in workload_batch:
        await job_queue.put(job)
        
    # Boot a dedicated engine processing node to track the items
    processor_node = asyncio.create_task(core_processor_node(job_queue, system_telemetry))
    
    # Wait for all tasks to filter through our defensive filters
    await job_queue.join()
    processor_node.cancel() # Tear down background engine loop
    
    # PRINT TELEMETRY SUMMARY REPORT
    print("\n" + "="*50)
    print("                SYSTEM AUDIT REPORT")
    print("="*50)
    print(f" Succeeded Tasks: {system_telemetry['SUCCEEDED']}")
    print(f" Timed Out Tasks: {system_telemetry['TIMED_OUT']}")
    print(f" Crashed Tasks:   {system_telemetry['FAILED']}")
    print("="*50)
    print(f"Total Engine Real-World Execution Window: {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())