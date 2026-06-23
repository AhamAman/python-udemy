import threading
import time
import random

# Coordination Primitives
start_gate_event = threading.Event()
finish_line_barrier = threading.Barrier(parties=3) # Expecting exactly 3 racer threads

def racer_worker(racer_name):
    print(f"  [Ready] {racer_name} is standing at the starting line...")
    
    # 1. EVENT WAIT: All threads block here until the event is fired (.set())
    start_gate_event.wait()
    
    print(f"  [RUNNING] {racer_name} is running!")
    time.sleep(random.uniform(1.0, 2.5)) # Simulating random running times
    
    print(f"  [ARRIVED] {racer_name} reached the finish line. Waiting for others...")
    
    # 2. BARRIER WAIT: Threads block here until the 3rd thread arrives
    finish_line_barrier.wait()
    
    # This line executes only AFTER all 3 threads have cleared the barrier
    print(f"  [EXIT] {racer_name} is walking away to the medal ceremony.")

if __name__ == "__main__":
    print("=== ORCHESTRATING COORDINTATION PRIMITIVES ===")
    
    # Spin up 3 distinct racer threads
    racers = ["Racer-A", "Racer-B", "Racer-C"]
    threads = []
    
    for name in racers:
        t = threading.Thread(target=racer_worker, args=(name,))
        threads.append(t)
        t.start()
        
    time.sleep(2)
    print("\n[Main Thread] Fire! Opening the start gate event...")
    
    # Wake up all threads waiting on this event simultaneously
    start_gate_event.set() 
    
    for t in threads:
        t.join()
        
    print("\n=== RACE CONCLUDED ===")