import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")


'''
Example 2
'''

import os
import threading
import time

def worker_thread(thread_name):
    # This variable lives on this thread's local stack frame
    local_variable = f"I am local to {thread_name}"
    
    print(f"\n--- {thread_name} Started ---")
    print(f"Parent Process ID (PID): {os.getpid()}")
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Memory Address of local_variable: {hex(id(local_variable))}")
    
    # Keep the thread alive for a moment
    time.sleep(5)

if __name__ == "__main__":
    print(f"=== MAIN PROGRAM STARTING ===")
    print(f"Main Process ID (PID): {os.getpid()}")
    
    # 1. Create a heap-allocated style object in Python (Shared by threads)
    shared_heap_object = ["Apple", "Banana", "Cherry"]
    print(f"Shared Object Memory Address (Heap): {hex(id(shared_heap_object))}")
    
    # 2. Spawn two separate threads inside this SAME process
    t1 = threading.Thread(target=worker_thread, args=("Thread-1",), name="Thread-1")
    t2 = threading.Thread(target=worker_thread, args=("Thread-2",), name="Thread-2")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print(f"\n=== MAIN PROGRAM ENDING ===")