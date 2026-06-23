import threading
import time
import random

class FutureClone:
    def __init__(self):
        # The internal gatekeeper coordination primitive
        self._condition = threading.Condition()
        
        # State Machine Tracking: PENDING -> RUNNING -> (FINISHED or EXCEPTION)
        self._state = "PENDING"
        self._result = None
        self._exception = None

    def result(self, timeout=None):
        """
        Synchronous, blocking boundary. 
        Forces the calling thread to wait until the box is filled.
        """
        with self._condition:
            # If the background worker hasn't resolved the state yet, sleep the thread
            while self._state not in ("FINISHED", "EXCEPTION"):
                print(f"[{threading.current_thread().name}] result() called but state is {self._state}. Going to sleep...")
                
                # wait() atomically releases the lock and puts this thread into a BLOCKED state
                stats = self._condition.wait(timeout=timeout)
                
                if not stats:
                    raise TimeoutError("The execution frame timed out before resolving.")
            
            print(f"[{threading.current_thread().name}] Woke up! State is now {self._state}. Unpacking data...")
            
            # If the worker encountered an exception, marshal and raise it here
            if self._exception:
                raise self._exception
                
            return self._result

    def _set_result(self, result):
        """Called by a background worker thread to fulfill the data contract."""
        with self._condition:
            self._result = result
            self._state = "FINISHED"
            # Signal the OS scheduler to wake up ALL threads sleeping on this condition
            self._condition.notify_all()

    def _set_exception(self, exception):
        """Called by a background worker thread if the execution crashes."""
        with self._condition:
            self._exception = exception
            self._state = "EXCEPTION"
            self._condition.notify_all()


# =====================================================================
# SIMULATING THE HANDSHAKE
# =====================================================================
def fake_worker_thread(future_receipt, should_crash=False):
    print(f"\n[{threading.current_thread().name}] Worker popped task! Changing state to RUNNING...")
    with future_receipt._condition:
        future_receipt._state = "RUNNING"
        
    # Simulate heavy processing time
    time.sleep(2)
    
    try:
        if should_crash:
            raise RuntimeError("Database connection timed out mid-transaction!")
        
        print(f"[{threading.current_thread().name}] Work complete. Pushing result into the Future box...")
        future_receipt._set_result("📦 Clean Payload Data")
    except Exception as err:
        print(f"[{threading.current_thread().name}] Crash detected! Pushing exception into the Future box...")
        future_receipt._set_exception(err)

if __name__ == "__main__":
    print("=== SCENARIO 1: SUCCESSFUL RESOLUTION ===")
    future_box = FutureClone()
    
    # Spawn a background thread and hand it the unpopulated future receipt box
    worker = threading.Thread(target=fake_worker_thread, args=(future_box, False), name="WorkerThread")
    worker.start()
    
    # Give the worker a split second to spin up
    time.sleep(0.1)
    
    # Main thread attempts to read data immediately
    print(f"[{threading.current_thread().name}] Querying future block...")
    output = future_box.result()
    print(f"[{threading.current_thread().name}] Success! Retrieved: {output}\n")
    worker.join()


    print("=== SCENARIO 2: EXCEPTION MARSHALING ===")
    broken_future_box = FutureClone()
    
    broken_worker = threading.Thread(target=fake_worker_thread, args=(broken_future_box, True), name="BrokenWorkerThread")
    broken_worker.start()
    
    time.sleep(0.1)
    
    print(f"[{threading.current_thread().name}] Querying broken future block...")
    try:
        output = broken_future_box.result()
    except RuntimeError as ex:
        print(f"[{threading.current_thread().name}] Trapped marshaled worker exception inside main context: {ex}")
        
    broken_worker.join()