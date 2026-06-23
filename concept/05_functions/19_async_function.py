import asyncio
import time

# ==========================================
# 1. Asynchronous Non-Blocking Coroutines
# ==========================================
async def simulate_network_fetch(endpoint_id: str, network_latency: float) -> dict:
    """Simulates a non-blocking network API call."""
    print(f"  [START] Fetching data from source: {endpoint_id}...")
    
    # Crucial: asyncio.sleep is a NON-BLOCKING pause. 
    # It yields the CPU pointer back to the event loop engine.
    await asyncio.sleep(network_latency)
    
    print(f"  [COMPLETE] Source {endpoint_id} packet received.")
    return {"endpoint": endpoint_id, "status": "200 OK"}


# ==========================================
# 2. Coordinating Concurrent Execution Chains
# ==========================================
async def main_application_pipeline():
    """Root coroutine managing the concurrent execution chain."""
    print("Initializing Asynchronous Network IO Pipeline...")
    start_time = time.perf_counter()
    
    # Schedule three distinct network requests to run CONCURRENTLY
    # The event loop schedules all three and hops between them as they await
    batch_results = await asyncio.gather(
        simulate_network_fetch("Node_Alpha", network_latency=2.0),
        simulate_network_fetch("Node_Beta",  network_latency=1.0),
        simulate_network_fetch("Node_Gamma", network_latency=1.5),
    )
    
    duration = time.perf_counter() - start_time
    print(f"\nPipeline Resolution: Processed {len(batch_results)} payloads.")
    # Total duration matches the slow SINGLE longest latency task (2.0s), 
    # not the cumulative sum of all tasks (2.0 + 1.0 + 1.5 = 4.5s)!
    print(f"Total Asynchronous processing execution time: {duration:.4f} seconds")


# ==========================================
# 3. Execution Entry Point
# ==========================================
# Spin up the native low-level event loop engine to process our core coroutine
asyncio.run(main_application_pipeline())