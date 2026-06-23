import functools
import time

# ==========================================
# 1. CLASS DECORATOR WITHOUT ARGUMENTS (Stateful)
# ==========================================
class CallCounter:
    def __init__(self, func):
        """
        When used as @CallCounter, Python passes the target function 
        directly to __init__ at decoration time.
        """
        self.func = func
        self.count = 0  # Internal state storage
        functools.update_wrapper(self, func) # Keeps function metadata intact

    def __call__(self, *args, **kwargs):
        """Executed every time the decorated function is called."""
        self.count += 1
        print(f"\n[Counter] '{self.func.__name__}' has been called {self.count} time(s).")
        return self.func(*args, **kwargs)


# ==========================================
# 2. CLASS DECORATOR WITH ARGUMENTS (Configurable + Stateful)
# ==========================================
class RateLimiter:
    def __init__(self, max_calls: int, period: float):
        """
        When arguments are passed (@RateLimiter(max_calls=2, period=5)),
        Python passes THOSE arguments here at decoration time. 
        The function is NOT passed here.
        """
        self.max_calls = max_calls
        self.period = period
        self.timestamps = [] # Stateful list to track call times

    def __call__(self, func):
        """
        Because __init__ received the config parameters, Python calls 
        __call__ immediately afterwards and passes the target function.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Filter out timestamps older than our time window
            self.timestamps = [t for t in self.timestamps if current_time - t < self.period]
            
            if len(self.timestamps) >= self.max_calls:
                print(f"[RateLimiter] Blocked! Max {self.max_calls} calls per {self.period}s allowed.")
                return "429 Too Many Requests"
            
            self.timestamps.append(current_time)
            return func(*args, **kwargs)
            
        return wrapper # Must return a callable wrapper


# ==========================================
# 3. APPLYING AND RUNNING THE DECORATORS
# ==========================================
print("--- PHASE 1: Decorating Functions ---")

@CallCounter
def process_payment(amount):
    print(f"   Processing payment of ${amount}...")
    return "Success"

# Only allows 2 calls every 2 seconds
@RateLimiter(max_calls=2, period=2.0)
def fetch_secure_data():
    print("   Fetching sensitive API data...")
    return "Data Payload"


print("\n--- PHASE 2: Execution ---")

# Test 1: Stateful Counter
process_payment(100)
process_payment(250)
print(f"Total counted directly from object state: {process_payment.count}")

# Test 2: Configurable Rate Limiter
print("\n>>> Call 1:")
print(f"Result: {fetch_secure_data()}")

print("\n>>> Call 2:")
print(f"Result: {fetch_secure_data()}")

print("\n>>> Call 3 (Should be blocked instantly):")
print(f"Result: {fetch_secure_data()}")

print("\n>>> Call 4 (After waiting 2 seconds):")
time.sleep(2.1)
print(f"Result: {fetch_secure_data()}")