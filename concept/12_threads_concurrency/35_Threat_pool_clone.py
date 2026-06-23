import threading
import queue
import time
import random

class FutureClone:
    def __init__(self):
        # Internal synchronization primitive to coordinate thread blocking
        self._condition = threading.Condition()
        self._state = "PENDING"
        self._result = None
        self._exception = None

    def result(self, timeout=None):
        """Blocks the calling thread until the worker fills this receipt."""
        with self._condition:
            # If the background thread isn't finished yet, sleep and yield the CPU
            while self._state not in ("FINISHED", "EXCEPTION"):
                # wait() temporarily releases the lock so the worker can modify the state
                if not self._condition.wait(timeout=timeout):
                    raise TimeoutError("Future result timed out.")
            
            # If the task crashed on the background thread, marshal and throw it here
            if self._exception:
                raise self._exception
                
            return self._result

    def _set_result(self, result):
        """Called internally by a worker thread to resolve the future successfully."""
        with self._condition:
            self._result = result
            self._state = "FINISHED"
            # Wake up any threads blocked at the .result() checkpoint
            self._condition.notify_all()

    def _set_exception(self, exception):
        """Called internally by a worker thread if the user's function crashes."""
        with self._condition:
            self._exception = exception
            self._state = "EXCEPTION"
            self._condition.notify_all()


class ThreadPoolExecutorClone:
    def __init__(self, max_workers):
        self._max_workers = max_workers
        self._work_queue = queue.Queue()
        self._workers = []
        self._shutdown_requested = False
        self._shutdown_lock = threading.Lock()
        
        # Pre-spawn permanent, reusable background worker threads
        for i in range(max_workers):
            t = threading.Thread(target=self._worker_loop, args=(i + 1,), daemon=True)
            self._workers.append(t)
            t.start()

    def _worker_loop(self, worker_id):
        """The core consumer execution loop running permanently on each thread."""
        while True:
            # Pull a work item. A work item is a tuple: (FutureClone, Function, Args, Kwargs)
            work_item = self._work_queue.get()
            
            # POISON PILL: If we extract None, it means the executor is shutting down cleanly
            if work_item is None:
                self._work_queue.task_done()
                break
                
            future, fn, args, kwargs = work_item
            
            # Transition state to active execution
            with future._condition:
                future._state = "RUNNING"
                
            try:
                # Execute the arbitrary business logic computation payload
                execution_output = fn(*args, **kwargs)
                future._set_result(execution_output)
            except Exception as e:
                # Trap the failure securely so the worker thread doesn't die completely
                future._set_exception(e)
            finally:
                self._work_queue.task_done()
                
        print(f"  [Worker-{worker_id}] Thread shutdown cleanly and reclaims stack space.")

    def submit(self, fn, *args, **kwargs):
        """Non-blocking interface. Places work on the queue and returns a Future receipt."""
        with self._shutdown_lock:
            if self._shutdown_requested:
                raise RuntimeError("Cannot submit new tasks after executor shutdown.")
                
            # Create the unpopulated Future placeholder receipt
            future = FutureClone()
            
            # Package the execution unit frame and drop it into our thread-safe queue channel
            self._work_queue.put((future, fn, args, kwargs))
            return future

    def shutdown(self, wait=True):
        """Gracefully signals workers to complete active tasks and spin down."""
        with self._shutdown_lock:
            if self._shutdown_requested:
                return
            self._shutdown_requested = True
            
        # Dispense exactly one poison pill (None) for each worker thread in our pool
        for _ in range(self._max_workers):
            self._work_queue.put(None)
            
        if wait:
            # Synchronize: block until all running and queued tasks are completely drained
            for t in self._workers:
                t.join()


# =====================================================================
# TESTING THE CLONE
# =====================================================================
def intensive_business_logic(task_name, duration):
    print(f"    [Processing] Executing task: '{task_name}'...")
    time.sleep(duration)
    
    if task_name == "Task-3":
        raise ZeroDivisionError("Simulated critical math failure inside Task-3!")
        
    return f"Polished-{task_name}-Payload"

if __name__ == "__main__":
    print("=== LAUNCHING THREAD POOL EXECUTOR CLONE (2 WORKERS) ===")
    pool = ThreadPoolExecutorClone(max_workers=2)
    
    # Submit tasks asynchronously
    future_1 = pool.submit(intensive_business_logic, "Task-1", 1.0)
    future_2 = pool.submit(intensive_business_logic, "Task-2", 0.5)
    future_3 = pool.submit(intensive_business_logic, "Task-3", 0.8) # Will crash
    
    print("\n[Main Thread] Tasks submitted successfully! Non-blocking pathway confirmed.")
    print("Main thread is completely free to do other work while tasks run background...\n")
    time.sleep(0.2)
    
    # Extract results. This will block on the main thread until the worker fulfills the receipt.
    print(f"[Main Extracting] Future-1 Result: {future_1.result()}")
    print(f"[Main Extracting] Future-2 Result: {future_2.result()}")
    
    print("\n[Main Extracting] Future-3 (Testing Exception Marshaling)...")
    try:
        data = future_3.result()
    except ZeroDivisionError as err:
        print(f" -> Success! Trapped background thread crash safely inside main thread: {err}")
        
    print("\nInitiating system pool cleanup...")
    pool.shutdown(wait=True)
    print("=== PIPELINE COMPLETELY RECLAIMED ===")