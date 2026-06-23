import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def api_query_provider(provider_name):
    # Simulate erratic external endpoint latency
    latency = random.uniform(0.5, 2.5)
    time.sleep(latency)
    
    # Simulate a downstream API server error on one specific source
    if provider_name == "Provider-Delta":
        raise ConnectionResetError("Remote API server dropped connection frame!")
        
    mock_ticket_price = round(random.uniform(250, 600), 2)
    return {"provider": provider_name, "price": mock_ticket_price, "speed": latency}

if __name__ == "__main__":
    print("=== LAUNCHING REAL-TIME AGGREGATION LOOKUP LOOP ===")
    global_start = time.time()
    
    api_providers = ["Provider-United", "Provider-Emirates", "Provider-Delta", "Provider-Lufthansa"]
    future_to_provider = {}
    
    with ThreadPoolExecutor(max_workers=4) as pool:
        # 1. SCATTER: Submit all tasks immediately and retain future maps
        for name in api_providers:
            future_object = pool.submit(api_query_provider, name)
            # Map the future object to the original string name for tracking
            future_to_provider[future_object] = name
            
        print("All API query requests dispatched. Listening for raw stream responses...\n")
        
        # 2. GATHER: Loop asynchronously as tasks finish executing
        # as_completed acts as an internal event yield engine
        for completed_future in as_completed(future_to_provider):
            provider_name = future_to_provider[completed_future]
            
            try:
                # Extract value. Will not block since as_completed guarantees it is done
                result = completed_future.result()
                print(f" [STREAM OUT] {result['provider']}: ${result['price']} (Resolved in {result['speed']:.2f}s)")
            except Exception as exc:
                # Safely capture background network errors without halting the other threads
                print(f" [STREAM ERROR] Failed to aggregate data from {provider_name} -> Reason: {exc}")
                
    print(f"\nAll streams closed. Final lifecycle aggregation window closed in {time.time() - global_start:.2f}s")