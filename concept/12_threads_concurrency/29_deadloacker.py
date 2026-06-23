import threading
import time

# Two independent critical resource locks
lock_alpha = threading.Lock()
lock_beta = threading.Lock()

def resource_scout_one():
    print("[Thread-1] Attempting to acquire Lock Alpha...")
    with lock_alpha:
        print("[Thread-1] Securely holding Lock Alpha. Simulating data parse...")
        time.sleep(1) # Window for Thread-2 to acquire Lock Beta
        
        print("[Thread-1] Now attempting to acquire Lock Beta...")
        with lock_beta:
            print("[Thread-1] Success! Cleared critical section.")

def resource_scout_two():
    print("  [Thread-2] Attempting to acquire Lock Beta...")
    with lock_beta:
        print("  [Thread-2] Securely holding Lock Beta. Simulating data parse...")
        time.sleep(1) # Window for Thread-1 to acquire Lock Alpha
        
        print("  [Thread-2] Now attempting to acquire Lock Alpha...")
        with lock_alpha:
            print("  [Thread-2] Success! Cleared critical section.")

if __name__ == "__main__":
    print("=== DEPLOYING MUTUAL LOOP DEPENDENCY (DEADLOCK) ===")
    
    t1 = threading.Thread(target=resource_scout_one)
    t2 = threading.Thread(target=resource_scout_two)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # Execution will NEVER reach this line
    print("=== LIFECYCLE COMPLETED CLEANLY ===")