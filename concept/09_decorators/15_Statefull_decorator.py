import functools
import time

# ==========================================
# 1. CLOSURE-BASED STATEFUL DECORATOR
# ==========================================
def track_usage(func):
    """Tracks how many times a function is called using a closure."""
    call_count = 0  # State variable inside outer scope
    history = []    # Tracks call timestamps

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Crucial: 'nonlocal' allows us to modify the mutable/immutable 
        # variables living inside the outer function's scope.
        nonlocal call_count
        call_count += 1
        
        current_time = time.strftime("%H:%M:%S")
        history.append(current_time)
        
        print(f"\n[Usage Tracker] '{func.__name__}' called (Total: {call_count} times)")
        print(f"                Timestamp History: {history}")
        
        return func(*args, **kwargs)
        
    return wrapper


# ==========================================
# 2. CLASS-BASED STATEFUL DECORATOR
# ==========================================
class MemoizeCache:
    """Caches deterministic function outputs to optimize performance."""
    def __init__(self, func):
        self.func = func
        self.cache = {}  # Clean, explicit instance-level state storage
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        """Executed whenever the decorated function is invoked."""
        # Using the positional arguments tuple as a dictionary key
        if args in self.cache:
            print(f"\n[Cache HIT] Returning cached results for arguments: {args}")
            return self.cache[args]
            
        print(f"\n[Cache MISS] Computing new results for arguments: {args}...")
        result = self.func(*args)
        self.cache[args] = result  # Mutating internal state
        return result


# ==========================================
# 3. RUNNING THE STATEFUL DECORATORS
# ==========================================
print("--- Test 1: Closure-Based Usage Tracker ---")

@track_usage
def fetch_user_profile(user_id):
    return f"Profile data for User {user_id}"

# Triggering execution to watch state accumulate
fetch_user_profile(101)
time.sleep(1)
fetch_user_profile(102)


print("\n--- Test 2: Class-Based Memoization Cache ---")

@MemoizeCache
def expensive_calculation(n):
    """Simulates a heavy mathematical operations."""
    time.sleep(1) # Simulated delay
    return n * n

# Call 1: Misses cache, computes
start = time.time()
print(f"Result: {expensive_calculation(5)} (Took {time.time() - start:.2f}s)")

# Call 2: Hits cache instantly
start = time.time()
print(f"Result: {expensive_calculation(5)} (Took {time.time() - start:.2f}s)")

# Call 3: Different input, misses cache
start = time.time()
print(f"Result: {expensive_calculation(10)} (Took {time.time() - start:.2f}s)")

# Introspecting the state explicitly from outside
print(f"\nExposed internal cache dictionary: {expensive_calculation.cache}")

