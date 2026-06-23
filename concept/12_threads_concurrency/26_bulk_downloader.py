import time
import requests
from concurrent.futures import ThreadPoolExecutor

# A batch of deterministic latency mock endpoints
URL_RESOURCES = [
    "https://httpbin.org/delay/0.5",
    "https://httpbin.org/delay/1.2",
    "https://httpbin.org/delay/0.3",
    "https://httpbin.org/delay/0.8"
]

def fetch_asset_worker(url):
    print(f"  [Worker Engine] Connecting to -> {url}")
    start = time.time()
    
    # Network I/O blocking call
    response = requests.get(url)
    
    elapsed = time.time() - start
    print(f"  [Worker Engine] Completed target fetch in {elapsed:.2f}s")
    return len(response.text)

def run_bulk_download_pipeline():
    print("=== INITIALIZING CONTAINERIZED BULK DOWNLOAD MATRIX ===")
    start_time = time.time()
    
    # Cap our maximum physical concurrency to exactly 3 workers
    with ThreadPoolExecutor(max_workers=3) as executor:
        print("Mapping source resources across worker matrix layer...\n")
        
        # .map handles queue tracking and item distribution under the hood implicitly
        results_iterator = executor.map(fetch_asset_worker, URL_RESOURCES)
        
        # Extract the values from the returned iterator
        # The main thread blocks here as needed, yielding values in input order
        payload_sizes = list(results_iterator)
        
    print("\n================ TELEMETRY DASHBOARD ================")
    print(f" Ordered Result Sizes: {payload_sizes}")
    print(f" Total Multi-threaded Pipeline Execution Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    run_bulk_download_pipeline()