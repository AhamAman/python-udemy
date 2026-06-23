import threading
import time
import os

# Configuration
NUM_FILES = 20
FILE_PREFIX = "dummy_data_"

def setup_dummy_files():
    print("Generating dummy text files on disk...")
    for i in range(NUM_FILES):
        with open(f"{FILE_PREFIX}{i}.txt", "w") as f:
            # Write 100,000 lines of text to ensure it takes actual disk read time
            f.write("Analyzing OS scheduling paradigms from first principles.\n" * 100_000)

def cleanup_files():
    for i in range(NUM_FILES):
        try:
            os.remove(f"{FILE_PREFIX}{i}.txt")
        except FileNotFoundError:
            pass
    print("Cleanup complete.")

def read_file_worker(filename, results_dict):
    start = time.time()
    
    # Perform disk read
    with open(filename, "r") as f:
        data = f.read()
        word_count = len(data.split())
        
    # Safely assign result to a unique entry in the dictionary
    results_dict[filename] = word_count
    # Print execution check
    # print(f"  [Thread] Processed {filename} in {time.time() - start:.3f}s")

def run_parallel_reader():
    print(f"\nProcessing {NUM_FILES} files using 4 worker threads concurrently...")
    start = time.time()
    
    results = {}
    threads = []
    
    # Chunk files into 4 distinct lists, one for each worker thread
    num_workers = 4
    file_chunks = [[] for _ in range(num_workers)]
    for i in range(NUM_FILES):
        file_chunks[i % num_workers].append(f"{FILE_PREFIX}{i}.txt")
        
    # Target function that wraps the chunk allocation logic
    def chunk_processor(files):
        for filename in files:
            read_file_worker(filename, results)

    # Launching the 4 worker threads
    for i in range(num_workers):
        t = threading.Thread(target=chunk_processor, args=(file_chunks[i],))
        threads.append(t)
        t.start()

    # Synchronizing: block main thread execution until all workers complete their chunks
    for t in threads:
        t.join()
        
    print(f"All workers finished. Total Processing Time: {time.time() - start:.3f} seconds.")
    print(f"Total words counted across all files: {sum(results.values()):,}")

if __name__ == "__main__":
    setup_dummy_files()
    try:
        run_parallel_reader()
    finally:
        cleanup_files()