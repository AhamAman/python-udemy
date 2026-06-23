import threading
import queue
import time

class EventDispatcher:
    def __init__(self):
        self._lock = threading.Lock()
        self._listeners = {} # Format: {"event_name": [callback_functions]}

    def subscribe(self, event_type, callback):
        with self._lock:
            if event_type not in self._listeners:
                self._listeners[event_type] = []
            self._listeners[event_type].append(callback)

    def dispatch(self, event_type, event_data):
        # Copy subscribers quickly under lock to minimize critical section hold
        targets = []
        with self._lock:
            if event_type in self._listeners:
                targets = list(self._listeners[event_type])
                
        # Fire handlers concurrently outside the lock to prevent blocking the dispatch engine
        for callback in targets:
            # Spawn a one-off thread or dispatch to an internal queue
            t = threading.Thread(target=callback, args=(event_data,))
            t.start()

# Mock listener targets running asynchronously
def analytics_handler(data):
    time.sleep(0.2)
    print(f"  [Analytics System Logged] User Event Tracking Details -> {data}")

def security_handler(data):
    print(f"  [Security Audit Active] Alert! Checking credentials for -> {data['username']}")

if __name__ == "__main__":
    print("=== INITIALIZING STATEFUL EVENT DISPATCHER ===")
    dispatcher = EventDispatcher()
    
    # Register listeners to the central registry
    dispatcher.subscribe("user_login", analytics_handler)
    dispatcher.subscribe("user_login", security_handler)
    
    print("Subscribers wired up cleanly. Dispatching 'user_login' event frame...")
    payload = {"username": "root_administrator", "ip_address": "127.0.0.1", "timestamp": time.time()}
    
    # The dispatcher decouples components completely
    dispatcher.dispatch("user_login", payload)
    
    print("[Main Loop] Dispatcher call finished instantly. Continuing application loop...")
    time.sleep(1) # Give background async handlers a window to print outputs