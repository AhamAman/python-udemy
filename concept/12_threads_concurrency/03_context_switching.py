import threading
import time

# Shared synchronization flags
lock = threading.Lock()
condition = threading.Condition(lock)
current_turn = 0
ITERATIONS = 100_000

def worker(thread_id):
    global current_turn
    next_thread = 1 if thread_id == 0 else 0
    
    for _ in range(ITERATIONS):
        with condition:
            # Wait until it is this thread's turn
            while current_turn != thread_id:
                condition.wait() # This forces the thread to yield and context switch
            
            # Pass the turn to the other thread and wake it up
            current_turn = next_thread
            condition.notify()

if __name__ == "__main__":
    print(f"Starting {ITERATIONS * 2:,} forced context switches...")
    
    t1 = threading.Thread(target=worker, args=(0,))
    t2 = threading.Thread(target=worker, args=(1,))
    
    start_time = time.time()
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    elapsed_time = time.time() - start_time
    # Total switches = ITERATIONS * 2 (each thread takes a turn per iteration)
    total_switches = ITERATIONS * 2
    avg_switch_time_ns = (elapsed_time / total_switches) * 1_000_000_000
    
    print("\n--- Benchmark Results ---")
    print(f"Total Time: {elapsed_time:.4f} seconds")
    print(f"Average Context Switch Time: {avg_switch_time_ns:.2f} nanoseconds")
    print(f"Average Context Switch Time: {avg_switch_time_ns / 1000:.2f} microseconds")