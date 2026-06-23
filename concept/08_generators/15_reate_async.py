import queue
import time

# -----------------------------------------------------------------
# 1. The Mock Async Operation (The Future)
# -----------------------------------------------------------------
class MockNetworkRequest:
    """Simulates a non-blocking background I/O operation."""
    def __init__(self, delay):
        self.target_time = time.time() + delay

    def is_ready(self):
        return time.time() >= self.target_time


# -----------------------------------------------------------------
# 2. The Yield-Based Async Functions
# -----------------------------------------------------------------
def async_fetch_user(user_id):
    print(f"📡 [Task {user_id}] Initiating API request...")
    request = MockNetworkRequest(delay=1.5)
    
    # This is exactly what `await request` does under the hood:
    # It yields the pending operation out to the event loop and pauses.
    while not request.is_ready():
        yield  # Yielding control back to the loop because we are waiting
        
    print(f"📥 [Task {user_id}] Network data arrived!")
    return {"user_id": user_id, "name": f"User_{user_id}"}


def async_main_orchestrator():
    print("🎬 [Main] Starting orchestration pipeline...")
    
    # Schedule two 'concurrent' network fetches
    task1 = async_fetch_user(101)
    task2 = async_fetch_user(202)
    
    # The event loop wrapper coordinates them
    yield ("SCHEDULE", task1)
    yield ("SCHEDULE", task2)


# -----------------------------------------------------------------
# 3. The Mini Event Loop
# -----------------------------------------------------------------
class MicroEventLoop:
    def __init__(self):
        self.task_queue = queue.Queue()

    def add_task(self, coro):
        self.task_queue.put(coro)

    def run(self):
        print("🌀 [Loop] Event Loop Started.")
        step = 0
        
        while not self.task_queue.empty():
            step += 1
            current_coro = self.task_queue.get()
            
            try:
                # Wake up the coroutine using send(None) (the equivalent of next())
                signal = current_coro.send(None)
                
                # Check if the coroutine spawned a child task to schedule
                if isinstance(signal, tuple) and signal[0] == "SCHEDULE":
                    child_coro = signal[1]
                    self.add_task(child_coro)
                
                # Task isn't finished, put it back in the queue to poll later
                self.add_task(current_coro)
                
            except StopIteration as e:
                # A StopIteration means the function hit a return statement!
                # The return value is embedded inside the exception object.
                if e.value:
                    print(f"🔔 [Loop] Task completed execution. Result returned: {e.value}")
                    
            time.sleep(0.1)  # Small tick rate break to prevent CPU melting
            
        print(f"🏁 [Loop] All tasks finished cleanly after {step} iterations.")

# --- Run the Event Loop ---
if __name__ == "__main__":
    loop = MicroEventLoop()
    loop.add_task(async_main_orchestrator())
    loop.run()