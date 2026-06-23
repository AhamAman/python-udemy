import threading
import time

class SecureCounter:
    def __init__(self):
        self.value = 0
        # Initialize a primitive lock
        self.lock = threading.Lock()

    def increment(self):
        # Using a context manager ('with') automatically acquires the lock
        # and guarantees it will be released even if an error occurs.
        with self.lock:
            # --- CRITICAL SECTION START ---
            current = self.value
            time.sleep(0.000001)  # Context switch window
            self.value = current + 1
            # --- CRITICAL SECTION END ---

def worker(counter, updates):
    for _ in range(updates):
        counter.increment()

if __name__ == "__main__":
    counter = SecureCounter()
    threads = []
    num_threads = 5
    updates_per_thread = 100
    expected_total = num_threads * updates_per_thread
    
    print(f"Spawning {num_threads} threads under Lock protection...")
    
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(counter, updates_per_thread))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("\n--- Protected Counter Results ---")
    print(f"Expected Mathematical Value: {expected_total}")
    print(f"Actual Captured Value:       {counter.value}")
    print(f"Corruption Deficit:          {expected_total - counter.value}")