import threading
import time

# The target function our worker thread will run
def download_worker(file_id, download_speed="High"):
    print(f"  [Worker] Thread-{file_id} status changed to RUNNING.")
    print(f"  [Worker] Starting file download {file_id} at {download_speed} speed...")
    
    # Thread enters WAITING/BLOCKED state here while sleeping (simulating network delay)
    time.sleep(2) 
    
    print(f"  [Worker] Thread-{file_id} finished work and is terminating.")

if __name__ == "__main__":
    print("=== MAIN THREAD STARTING ===")
    
    # 1. NEW STATE
    # Creating the thread object. Note args must be a tuple: (value,)
    t1 = threading.Thread(
        target=download_worker, 
        args=(1,), 
        kwargs={"download_speed": "Maximum"},
        name="DownloadThread-1"
    )
    
    print("Main Thread created t1 (Status: NEW). It has not started yet.")
    time.sleep(1)
    
    # 2. RUNNABLE -> RUNNING STATE
    print("\nMain Thread calling t1.start()...")
    t1.start() # The OS scheduler takes over here
    
    # The Main Thread continues running independently alongside t1
    print("Main Thread is free to execute other instructions instantly...")
    for i in range(3):
        print(f"  [Main] Doing background UI rendering work... {i}")
        time.sleep(0.4)
        
    # 3. WAITING FOR SYNCHRONIZATION (JOIN)
    print("\nMain Thread hits t1.join(). It will now freeze until t1 completes.")
    t1.join() # Main thread goes to WAITING state until t1 enters TERMINATED state
    
    print("\nt1 has terminated. Main Thread resumes control.")
    print("=== MAIN THREAD ENDING ===")