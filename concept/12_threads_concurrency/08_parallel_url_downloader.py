import threading
import time
import requests

# A list of real endpoints that introduce a deterministic 1-second server delay
URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

def download_task(url, results, index):
    print(f"  [Thread-{index}] Starting download from: {url}")
    start = time.time()
    
    # This network I/O call blocks this specific worker thread
    response = requests.get(url)
    
    # Store the result back in a thread-safe distinct slot
    results[index] = len(response.text)
    print(f"  [Thread-{index}] Finished in {time.time() - start:.2f}s")

def run_sequential():
    print("\n--- Running Sequentially ---")
    start = time.time()
    results = [0] * len(URLS)
    
    for i, url in enumerate(URLS):
        download_task(url, results, i)
        
    print(f"Sequential Total Execution Time: {time.time() - start:.2f} seconds")

def run_parallel_threads():
    print("\n--- Running Concurrently with Multiple Workers ---")
    start = time.time()
    
    results = [0] * len(URLS)
    threads = []
    
    # 1. Thread Creation: Spawning a worker thread for each URL
    for i, url in enumerate(URLS):
        t = threading.Thread(target=download_task, args=(url, results, i))
        threads.append(t)
        t.start() # Moves the thread from New -> Runnable
        
    # 2. Thread Synchronization: Ensuring the main thread blocks until all workers are Terminated
    for t in threads:
        t.join()
        
    print(f"Parallel Total Execution Time: {time.time() - start:.2f} seconds")
    print(f"Downloaded payloads sizes: {results}")

if __name__ == "__main__":
    run_sequential()
    run_parallel_threads()