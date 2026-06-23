import time
import requests

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

def fetch_url_sequentially():
    print(f"=== STARTING SEQUENTIAL HTTP FETCH (Total: {len(URLS)} tasks) ===")
    start_time = time.time()
    
    for idx, url in enumerate(URLS, 1):
        print(f"  [Task-{idx}] Requesting data from network endpoint...")
        task_start = time.time()
        
        # This HTTP request is a BLOCKING call. 
        # The entire thread halts here waiting for bytes to travel over the wire.
        response = requests.get(url)
        
        task_duration = time.time() - task_start
        print(f"  [Task-{idx}] Response received! Status: {response.status_code} (Took {task_duration:.2f}s)")
        
    total_duration = time.time() - start_time
    print(f"\n❌ Pipeline Finished. Total Sequential Clock Time: {total_duration:.2f} seconds")

if __name__ == "__main__":
    fetch_url_sequentially()