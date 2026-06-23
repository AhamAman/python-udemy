import asyncio
import time
import httpx

# Shared tracking ledger for parsed data
scraped_data_lake = []

async def fetch_api_endpoint(client, target_id, semaphore):
    """
    Defensively queries an external HTTP endpoint using connection pooling,
    granule timeouts, and an architectural concurrency gate.
    """
    url = f"https://httpbin.org/delay/1" # Simulates a slow 1-second server response
    
    # Configure precise defensive timeout matrices (in seconds)
    timeout_policy = httpx.Timeout(total=3.0, connect=1.0, read=1.5)
    
    # Enforce our semaphore concurrency gate to control out-of-process blast radius
    async with semaphore:
        print(f"  [Gate Passed] [Task-{target_id}] Dispatching connection request over connection pool...")
        start_time = time.time()
        
        try:
            # Reuses an established TCP connection socket out of the client pool matrix
            response = await client.get(url, timeouts=timeout_policy, params={"id": target_id})
            
            if response.status_code == 200:
                duration = time.time() - start_time
                print(f"  [Success]     [Task-{target_id}] Ingested bytes cleanly in {duration:.2f}s")
                return {"task_id": target_id, "status": "SUCCESS", "payload": response.json()['args']}
                
        except httpx.TimeoutException:
            print(f"  [FAIL ALERT]  [Task-{target_id}] Read/Connect timeout threshold tripped!")
            return {"task_id": target_id, "status": "TIMEOUT", "payload": None}
        except httpx.HTTPError as err:
            print(f"  [FAIL ALERT]  [Task-{target_id}] Transport error encountered: {err}")
            return {"task_id": target_id, "status": "HTTP_ERROR", "payload": None}

async def main():
    print("=== INITIALIZING CONCURRENT HTTP CLIENT ARCHITECTURE ===\n")
    global_start = time.time()
    
    # 1. Establish a Semaphore limit to throttle maximum concurrent sockets to 3
    concurrency_gate = asyncio.Semaphore(3)
    
    # 2. Instantiate a reusable AsyncClient context manager. 
    # This automatically activates Connection Pooling under the hood.
    async with httpx.AsyncClient(limits=httpx.Limits(max_connections=10)) as shared_pool_client:
        
        print("[Main] Fan-Out Phase: Enqueueing 10 HTTP requests into the event loop...")
        # Create 10 concurrent lookup tasks sharing the exact same client and pool
        task_batch = [
            asyncio.create_task(fetch_api_endpoint(shared_pool_client, i, concurrency_gate))
            for i in range(1, 11)
        ]
        
        print("[Main] Fan-In Phase: Gathering aggregated data streams...")
        # Unpack concurrent executions and flatten results
        compiled_responses = await asyncio.gather(*task_batch)
        
    print("\n================ DATA COMPILER AUDIT REPORT ================")
    print(f"Total Jobs Handled: {len(compiled_responses)}")
    
    success_count = sum(1 for r in compiled_responses if r['status'] == "SUCCESS")
    print(f"Successful Ingestions: {success_count} / 10")
    print(f"Total Pipeline Processing Clock Time: {time.time() - global_start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())