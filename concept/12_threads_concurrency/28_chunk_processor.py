import time
import random
from concurrent.futures import ThreadPoolExecutor

def generate_mock_log_data():
    # Simulate generating a large log file array directly in heap memory
    levels = ["INFO", "WARN", "ERROR", "DEBUG"]
    return [f"2026-06-23 [{random.choice(levels)}] System execution heartbeat token frame." for _ in range(100_000)]

def parse_chunk_worker(chunk_id, log_chunk_slice):
    # Each thread handles a completely isolated data array block slice
    # print(f"  [Thread Work] Worker-{chunk_id} analyzing slice block containing {len(log_chunk_slice):,} rows...")
    error_count = 0
    for line in log_chunk_slice:
        if "[ERROR]" in line:
            error_count += 1
    return error_count

def run_parallel_log_analytics():
    print("=== INITIALIZING CONCURRENT LOG ANALYTICS MACHINE ===")
    raw_logs = generate_mock_log_data()
    print(f"Loaded {len(raw_logs):,} raw log entries into heap address memory space.")
    
    start_time = time.time()
    
    # Chunking Strategy: Segment the 100,000 logs into 4 equal blocks of 25,000
    chunk_size = 25_000
    log_chunks = [raw_logs[i:i + chunk_size] for i in range(0, len(raw_logs), chunk_size)]
    
    futures_list = []
    
    # Spin up 4 threads to map exactly to our 4 discrete memory blocks
    with ThreadPoolExecutor(max_workers=4) as executor:
        for idx, chunk in enumerate(log_chunks, 1):
            # Pass the isolated chunk data explicitly into the executor
            f = executor.submit(parse_chunk_worker, idx, chunk)
            futures_list.append(f)
            
        # Gather results by forcing a blocking summary calculation loop
        total_errors_detected = sum(f.result() for f in futures_list)
        
    print("\n================ ANALYSIS TELEMETRY ================")
    print(f" Total Log Entries Scanned:  {len(raw_logs):,}")
    print(f" Total [ERROR] Tags Found:  {total_errors_detected:,}")
    print(f" Total Map-Reduce Profiling Time: {time.time() - start_time:.4f} seconds")

if __name__ == "__main__":
    run_parallel_log_analytics()