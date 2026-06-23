import threading
import time

class BrokenCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # 1. READ: Pull current value from shared memory
        current = self.value
        
        # Simulating slight processing latency or an OS context switch window
        time.sleep(0.000001)
        
        # 2. MODIFY & 3. WRITE: Push updated value back to shared memory
        self.value = current + 1

def worker(counter, updates):
    for _ in range(updates):
        counter.increment()

if __name__ == "__main__":
    counter = BrokenCounter()
    threads = []
    num_threads = 5
    updates_per_thread = 100
    
    expected_total = num_threads * updates_per_thread
    print(f"Spawning {num_threads} threads, each incrementing {updates_per_thread} times...")
    
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(counter, updates_per_thread))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("\n--- Counter Simulation Results ---")
    print(f"Expected Mathematical Value: {expected_total}")
    print(f"Actual Captured Value:       {counter.value}")
    print(f"Corruption Deficit:          {expected_total - counter.value}")