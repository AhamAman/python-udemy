import collections
import time

class MockCoroutine:
    """A first-principles representation of a stateful coroutine function."""
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps
        self.current_step = 0

    def resume(self):
        """Advances the coroutine execution state up to its next yield checkpoint."""
        if self.current_step >= len(self.steps):
            raise StopIteration("Coroutine completed naturally.")
            
        # Execute the current code block segment
        action_text, is_io_bound = self.steps[self.current_step]
        print(f"  [{self.name}] Executing: {action_text}")
        self.current_step += 1
        
        # Return True if this step simulates an I/O wait, signaling a yield requirement
        return is_io_bound


class ManualEventLoop:
    def __init__(self):
        # FIFO Ready Queue tracking tasks equipped to occupy the CPU right now
        self.ready_queue = collections.deque()
        
        # Waiting Queue tracking tasks paused while waiting for hardware/timers
        self.waiting_queue = []

    def add_task(self, coro):
        """Registers a coroutine wrapper directly into the active line."""
        self.ready_queue.append(coro)

    def run(self):
        print("=== BOOTING MANUAL EVENT LOOP INFRASTRUCTURE ===")
        tick = 0
        
        # Continue loop cycle as long as there is work anywhere in the system
        while self.ready_queue or self.waiting_queue:
            tick += 1
            print(f"\n--- Loop Tick #{tick} ---")
            
            # 1. SIMULATE THE OS NOTIFICATION WAKEUP
            # If tasks are in the waiting queue, simulate their I/O finishing after a brief delay
            if self.waiting_queue:
                # For this demo, we automatically wake up waiting tasks on the next tick
                ready_to_wake = list(self.waiting_queue)
                self.waiting_queue.clear()
                for task in ready_to_wake:
                    print(f"  [OS Kernel Signal] I/O bytes arrived for {task.name}! Moving back to Ready Queue.")
                    self.ready_queue.append(task)

            # 2. DISPATCH THE READY QUEUE TASKS
            # Capture the current tasks ready to run on this specific tick window
            batch_size = len(self.ready_queue)
            for _ in range(batch_size):
                if not self.ready_queue:
                    break
                    
                # Pop the oldest task from the ready queue
                active_task = self.ready_queue.popleft()
                
                try:
                    # Pass control of the single thread into the task
                    needs_io_wait = active_task.resume()
                    
                    if needs_io_wait:
                        # Task voluntarily hit a yield point. Move it to the waiting silo.
                        print(f"  [Yield] {active_task.name} is waiting for network I/O. Relinquishing control...")
                        self.waiting_queue.append(active_task)
                    else:
                        # Task ran a quick compute step. It goes straight to the back of the ready queue.
                        self.ready_queue.append(active_task)
                        
                except StopIteration:
                    print(f"  [Done] {active_task.name} has finished its execution path.")
                    
            # Micro-sleep to prevent pinning the hardware CPU at 100% during the simulation
            time.sleep(0.4)

        print("\n=== SYSTEM INVENTORY DRAINED: LOOP CLOSING ===")


if __name__ == "__main__":
    # Define tasks as a series of execution steps: (Display Text, Is It An I/O Operation?)
    task_alpha_steps = [
        ("Read local configuration file from disk cache", False),
        ("Initiate remote API connection request to fetch metrics", True),  # <-- Yield Point
        ("Parse returned network JSON telemetry payload matrix", False)
    ]
    
    task_beta_steps = [
        ("Render UI button frames and window baseline margins", False),
        ("Download user avatar profile picture image asset", True),       # <-- Yield Point
        ("Map image pixels directly onto global interface layout", False)
    ]

    # Initialize components
    loop = ManualEventLoop()
    
    coro1 = MockCoroutine("Task-Alpha", task_alpha_steps)
    coro2 = MockCoroutine("Task-Beta", task_beta_steps)
    
    # Load tasks into the scheduler loop
    loop.add_task(coro1)
    loop.add_task(coro2)
    
    # Give control of the main runtime thread over to the loop engine
    loop.run()