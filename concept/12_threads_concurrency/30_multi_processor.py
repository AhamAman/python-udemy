import multiprocessing
import threading
import time

# A global variable sitting on the main heap
shared_global_state = "ORIGINAL_SAFE_STATE"

def worker_logic(execution_type):
    global shared_global_state
    print(f"  [{execution_type} Worker] Accessing global state...")
    
    # Attempting to mutate the global state
    shared_global_state = f"MUTATED_BY_{execution_type.upper()}"
    print(f"  [{execution_type} Worker] Local updated state to: '{shared_global_state}'")

if __name__ == "__main__":
    # Must include this guard for Windows compatibility under multiprocessing!
    multiprocessing.freeze_support() 
    
    print("=== BEGINNING MEMORY ISOLATION EXPERIMENT ===")
    print(f"Starting Main Base State: '{shared_global_state}'\n")

    # 1. THE THREAD TEST (Shared Memory)
    print("--- Phase 1: Launching Thread ---")
    t = threading.Thread(target=worker_logic, args=("Thread",))
    t.start()
    t.join()
    print(f"[Main Process] State after thread exit: '{shared_global_state}'")
    print("Result: Threads share memory, so the state was permanently altered.\n")

    # Reset state
    shared_global_state = "ORIGINAL_SAFE_STATE"

    # 2. THE PROCESS TEST (Isolated Memory)
    print("--- Phase 2: Launching Process ---")
    p = multiprocessing.Process(target=worker_logic, args=("Process",))
    p.start()
    p.join()
    print(f"[Main Process] State after process exit: '{shared_global_state}'")
    print("Result: The process ran in a separate memory silo. The parent memory remains safe.")