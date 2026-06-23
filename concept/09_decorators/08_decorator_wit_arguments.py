import functools
import time

# ==========================================
# 1. THE DECORATOR FACTORY (Three-Layer Structure)
# ==========================================
print("--- Phase 1: Defining the Decorator Factory ---")

def monitor(min_level="INFO", max_retries=0):
    """
    A decorator factory that configures a logging and validation decorator.
    
    Layer 1 (monitor): Accepts configuration arguments.
    Layer 2 (decorator): Accepts the target function.
    Layer 3 (wrapper): Accepts the target function's arguments (*args, **kwargs).
    """
    print(f"[Execution Order - 1] Factory called with config: level={min_level}, retries={max_retries}")
    
    def decorator(func):
        print(f"[Execution Order - 2] Decorator wrapping function: '{func.__name__}'")
        
        # Common Mistake Fix: Always use @functools.wraps to preserve docstrings and function names
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n[Execution Order - 3] Wrapper executing before '{func.__name__}'")
            
            # --- Configurable Validation ---
            print(f"   [Validation] Checking if inputs are valid... (Min Level Required: {min_level})")
            if min_level == "CRITICAL" and not kwargs.get("is_urgent", False):
                print("   [Validation] FAILED: Non-urgent call blocked under CRITICAL level.")
                return "Blocked: Insufficient Urgency"
            
            # --- Configurable Execution / Retry Logic ---
            attempts = 0
            while attempts <= max_retries:
                try:
                    print(f"   [Logging] Attempt {attempts + 1} of {max_retries + 1}...")
                    result = func(*args, **kwargs)
                    print(f"   [Logging] Success! Result: {result}")
                    return result
                except Exception as e:
                    print(f"   [Logging] Caught exception: {e}")
                    attempts += 1
                    if attempts > max_retries:
                        print("   [Logging] Max retries reached. Raising error.")
                        raise e
                    print("   [Logging] Retrying...")
                    time.sleep(0.1)
                    
        return wrapper
    return decorator


# ==========================================
# 2. APPLYING THE DECORATOR (Compilation/Load Time)
# ==========================================
print("\n--- Phase 2: Decorating the Functions ---")

# Example A: Standard low-priority task with 2 retries if it fails
@monitor(min_level="INFO", max_retries=2)
def unstable_network_call(success=True):
    """Simulates a network call that might fail."""
    if not success:
        raise ConnectionError("Network timeout!")
    return "Data Fetched"

# Example B: A strict, critical task that requires urgency validation
@monitor(min_level="CRITICAL", max_retries=0)
def delete_database_records(is_urgent=False):
    return "Database Cleared"


# ==========================================
# 3. RUNNING THE CODE (Runtime)
# ==========================================
print("\n--- Phase 3: Runtime Execution ---")

# Test 1: Validation failure (Passing an argument that fails our decorator config)
print("\n>>> Running Test 1: Critical function without urgency flag...")
response1 = delete_database_records(is_urgent=False)
print(f"Final Return Value: {response1}")

# Test 2: Validation success
print("\n>>> Running Test 2: Critical function with urgency flag...")
response2 = delete_database_records(is_urgent=True)
print(f"Final Return Value: {response2}")

# Test 3: Logging & Retry logic triggering on failure
print("\n>>> Running Test 3: Unstable call failing then succeeding...")
# We will intentionally fail twice, then succeed on the 3rd attempt (retry 2)
# Since functions in Python are dynamic, we simulate this with a stateful list
failure_sequence = [False, False, True] 

@monitor(min_level="INFO", max_retries=2)
def flakey_api():
    if not failure_sequence.pop(0):
        raise ConnectionError("Flakey API dropped connection")
    return "API Success"

print("\nTriggering flakey_api:")
response3 = flakey_api()
print(f"Final Return Value: {response3}")