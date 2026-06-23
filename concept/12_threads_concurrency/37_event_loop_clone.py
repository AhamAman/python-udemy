import time
import heapq

class EventLoopClone:
    def __init__(self):
        # A priority queue tracking scheduled timers: (absolute_timestamp, callback)
        # Using a heap ensures the closest timer is always sitting at index 0
        self._timers = []
        
        # A simple list tracking active tasks (Python generators) running concurrently
        self._ready_tasks = []
        
        self._running = False

    def call_later(self, delay, callback, *args):
        """Schedules a synchronous callback to execute after a deterministic delay."""
        execution_time = time.time() + delay
        heapq.heappush(self._timers, (execution_time, callback, args))

    def create_task(self, generator):
        """Registers a cooperative generator function to run concurrently on the loop."""
        self._ready_tasks.append(generator)

    def run_forever(self):
        """The heart of the system: a continuous loop executing queued work blocks."""
        self._running = True
        print("=== EVENT LOOP CLONE BOOTED AND ACTIVE ===\n")
        
        while self._running:
            now = time.time()
            
            # 1. PROCESS TIMERS PHASE
            # Check if the closest timer in our priority queue is ready to fire
            while self._timers and self._timers[0][0] <= now:
                _, callback, args = heapq.heappop(self._timers)
                # Execute the callback synchronously
                callback(*args)

            # 2. PROCESS TASKS PHASE (Cooperative Multitasking Execution Loop)
            # Create a temporary working queue for this specific tick
            current_batch = list(self._ready_tasks)
            self._ready_tasks.clear()

            for task in current_batch:
                try:
                    # Advance the generator task forward to its next yield point
                    # This passes control inside the task code
                    next(task)
                    
                    # If the task yielded successfully without finishing,
                    # re-queue it to continue processing on the next iteration tick
                    self._ready_tasks.append(task)
                except StopIteration:
                    # The generator function hit a return statement and finished naturally
                    pass

            # 3. CONSERVATION CHECK
            # If nothing is scheduled and no tasks are active, shut down the loop
            if not self._timers and not self._ready_tasks:
                self._running = False
                
            # Prevent a tight loop from pinning the CPU at 100% when waiting for timers
            time.sleep(0.01)

        print("\n=== EVENT LOOP CLOSED AND RECLAIMED ===")


# =====================================================================
# SIMULATING ASYNCHRONOUS TASKS
# =====================================================================

def timer_alert_callback(message):
    print(f"  [Timer Interrupt Alert] Triggered: '{message}' at {time.time():.2f}")

def async_worker_one():
    print("[Task-1] Started execution loop segment A...")
    # yield hands execution control directly back to the Event Loop
    yield 
    
    print("[Task-1] Woke up for segment B. Processing data matrix elements...")
    yield
    
    print("[Task-1] Concluding task metrics.")

def async_worker_two():
    print("  [Task-2] Booted up. Performing initial network check...")
    yield
    
    print("  [Task-2] Network check cleared. Rendering user baseline state...")
    yield
    
    print("  [Task-2] Completed.")


if __name__ == "__main__":
    # Initialize our single-threaded concurrency engine
    loop = EventLoopClone()
    
    # Schedule delayed timer callbacks
    loop.call_later(0.5, timer_alert_callback, "Fast Notification Packet")
    loop.call_later(1.2, timer_alert_callback, "Slow Background Cleanup Job")
    
    # Register our concurrent generator tasks
    loop.create_task(async_worker_one())
    loop.create_task(async_worker_two())
    
    # Transfer control of the thread to the Event Loop
    loop.run_forever()