import threading
import time
import random

# A Semaphore that allows a maximum of 2 threads to hold the resource simultaneously
database_connection_pool = threading.Semaphore(value=2)

def access_database_worker(worker_id):
    print(f"  [Queue] Worker-{worker_id} wants to query the database.")
    
    # Decrements internal semaphore counter. If counter is 0, blocks here.
    with database_connection_pool:
        print(f"  ==> [ACQUIRED] Worker-{worker_id} secured a connection slot!")
        # Simulating active data query processing
        work_time = random.uniform(1.0, 2.0)
        time.sleep(work_time)
        print(f"  <== [RELEASED] Worker-{worker_id} finished. Leaving connection slot.")

if __name__ == "__main__":
    print("=== STARTING SEMAPHORE RESOURCE POOL CONTEXT ===")
    print("Total Available Connections: 2. Spawning 5 Worker Threads.\n")
    
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=access_database_worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("\n=== RESOURCE POOL DEMO COMPLETE ===")