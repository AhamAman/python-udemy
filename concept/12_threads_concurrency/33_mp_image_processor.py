import time
import random
from concurrent.futures import ProcessPoolExecutor, as_completed

def apply_heavy_filter_worker(image_name):
    print(f"  [PID Worker] Applying convolution matrix filters to {image_name}...")
    start = time.time()
    
    # Simulating heavy mathematical matrix loops per pixel
    # Generating 25 million random numbers to match intensive CPU computation cycles
    total_pixels = 25_000_000
    accumulator = 0
    for _ in range(total_pixels):
        accumulator += random.randint(1, 3)
        
    elapsed = time.time() - start
    return f"Polished_{image_name} (Processed in {elapsed:.2f}s)"

if __name__ == "__main__":
    image_gallery = [f"raw_capture_00{i}.png" for i in range(1, 5)]
    
    print("=== INITIALIZING CPU-BOUND IMAGE FILTER ENGINE ===")
    print(f"Images in queue: {image_gallery}\n")
    
    global_start = time.time()
    
    # Using submit() and as_completed() to capture finished files dynamically
    with ProcessPoolExecutor() as pool:
        future_tasks = [pool.submit(apply_heavy_filter_worker, img) for img in image_gallery]
        
        for completed_future in as_completed(future_tasks):
            output_payload = completed_future.result()
            print(f"  ==> [EXPORT SINK] Saved: {output_payload}")
            
    print(f"\nCompleted multi-process rendering grid in {time.time() - global_start:.2f} seconds.")