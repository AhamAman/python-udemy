import asyncio
import time
import random

async def download_file_worker(file_id, size_mb):
    # Simulating volatile network latency matching the asset file footprint
    simulated_download_time = size_mb * 0.5
    print(f"  [Downloader] Starting asset #{file_id} ({size_mb}MB) -> Estimated download window: {simulated_download_time:.2f}s")
    
    await asyncio.sleep(simulated_download_time)
    
    return f"asset_00{file_id}.jpg", size_mb

async def main():
    print("=== INITIALIZING CONCURRENT DOWNSTREAM DATA STREAM ===")
    start_time = time.time()
    
    # Mock data pool representing a batch of images to scrape: (file_id, size_in_mb)
    download_queue = [(1, 4.0), (2, 1.0), (3, 5.0), (4, 0.5)]
    
    # 1. FAN-OUT PHASE: Kick off all download tasks concurrently into the loop
    tasks = [asyncio.create_task(download_file_worker(fid, size)) for fid, size in download_queue]
    
    print(f"[Main Loop] {len(tasks)} tasks deployed to the ready queue. Intercepting completed frames on the fly...\n")
    
    total_bytes_processed = 0
    
    # 2. FAN-IN PHASE (Stream Optimization): Process assets dynamically as they finish
    for finished_future in asyncio.as_completed(tasks):
        # The line below blocks ONLY until the next closest worker reaches the DONE state
        filename, size = await finished_future
        
        total_bytes_processed += size
        print(f"  ==> [DISK WRITE SINK] Successfully flushed '{filename}' to /data/ storage bucket at {time.time() - start_time:.2f}s")
        
    print(f"\n⚡ Batch sync completed successfully.")
    print(f" Total Network Data Ingested: {total_bytes_processed} MB")
    print(f" Total Real-World Execution Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())