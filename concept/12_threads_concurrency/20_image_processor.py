import threading
import queue
import time
import random

# Cascading Pipeline Channels
download_to_filter_queue = queue.Queue(maxsize=2)
filter_to_upload_queue = queue.Queue(maxsize=2)

def image_downloader():
    images = ["photo_1.jpg", "photo_2.jpg", "photo_3.jpg"]
    for img in images:
        print(f"[STAGE 1] Downloading raw bytes for {img}...")
        time.sleep(random.uniform(0.2, 0.4)) # Simulate network I/O
        
        # Pass data forward to Stage 2's queue
        download_to_filter_queue.put(img)
        print(f"  -> Sent {img} to filter queue.")
        
    # Send poison pill to signal the down-stream filter stage that no more work is coming
    download_to_filter_queue.put(None)

def image_filter_transformer():
    while True:
        img = download_to_filter_queue.get()
        if img is None:
            download_to_filter_queue.task_done()
            break
            
        print(f"    [STAGE 2] Applying optimization filters to {img}...")
        time.sleep(random.uniform(0.5, 0.8)) # Simulate intensive CPU manipulation
        
        # Pass data forward to Stage 3's queue
        filter_to_upload_queue.put(img)
        download_to_filter_queue.task_done()
        
    # Send poison pill to upload stage
    filter_to_upload_queue.put(None)

def image_uploader():
    while True:
        img = filter_to_upload_queue.get()
        if img is None:
            filter_to_upload_queue.task_done()
            break
            
        print(f"        [STAGE 3] Uploading polished {img} to Cloud Storage AWS S3...")
        time.sleep(random.uniform(0.3, 0.6)) # Simulate network outbound I/O
        filter_to_upload_queue.task_done()

if __name__ == "__main__":
    print("=== STARTING MULTI-STAGE CONCURRENT IMAGE PIPELINE ===\n")
    start_time = time.time()
    
    # Create threads representing distinct production line machinery
    stage1 = threading.Thread(target=image_downloader)
    stage2 = threading.Thread(target=image_filter_transformer)
    stage3 = threading.Thread(target=image_uploader)
    
    # Start all machinery concurrently
    stage1.start()
    stage2.start()
    stage3.start()
    
    # Synchronize: Wait for all stages to conclude processing
    stage1.join()
    stage2.join()
    stage3.join()
    
    print(f"\nPipeline processing complete in {time.time() - start_time:.2f} seconds.")