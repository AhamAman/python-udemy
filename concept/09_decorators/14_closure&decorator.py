import functools

# ==========================================
# 1. UNDERSTANDING THE CLOSURE MEMORY CELL
# ==========================================
print("--- Phase 1: Pure Closure Mechanics ---")

def StateRetainer(initial_message):
    """A simple function that returns an inner function closing over data."""
    saved_state = initial_message  # Variable in the outer function's scope

    def inner_printer():
        # inner_printer 'closes over' the saved_state variable
        print(f"   [Closure Read] Retained message is: '{saved_state}'")
        
    return inner_printer

# Instantiate the closure
my_closure_instance = StateRetainer("Hello from the past!")

# The outer function 'StateRetainer' has completely finished executing here.
# Yet, look what happens when we invoke the inner instance:
my_closure_instance()

# Veteran Introspection: Let's peek into the actual memory cell structure of Python
print(f"   [Introspection] Does __closure__ exist? {my_closure_instance.__closure__ is not None}")
captured_value = my_closure_instance.__closure__[0].cell_contents
print(f"   [Introspection] Value frozen inside the closure cell: '{captured_value}'")


# ==========================================
# 2. THE DECORATOR FACTORY CLOSURE CHAIN
# ==========================================
print("\n--- Phase 2: Multi-Layer Closures in Decorators ---")

def speed_limit(max_allowed_kmh):
    """
    A Decorator Factory.
    Layer 1 (speed_limit): Captures the configuration variable `max_allowed_kmh`.
    """
    def decorator(func):
        """
        Layer 2 (decorator): Captures the target function object `func`.
        It also retains access to Layer 1's `max_allowed_kmh`.
        """
        @functools.wraps(func)
        def wrapper(current_speed, *args, **kwargs):
            """
            Layer 3 (wrapper): Executed at runtime. 
            It references values from BOTH outer scopes simultaneously.
            """
            print(f"\n[Wrapper Executing] Target: '{func.__name__}'")
            print(f"   Config check (Layer 1 Closure): Max allowed is {max_allowed_kmh} km/h")
            print(f"   Function check (Layer 2 Closure): Original function ID is {id(func)}")
            
            if current_speed > max_allowed_kmh:
                print(f"   [Alert] Speed {current_speed} km/h exceeds limit! Throttling...")
                current_speed = max_allowed_kmh
                
            # Executing the captured target function
            return func(current_speed, *args, **kwargs)
        return wrapper
    return decorator


# ==========================================
# 3. APPLYING THE CHAIN
# ==========================================

@speed_limit(max_allowed_kmh=120)
def drive_car(speed):
    return f"Car traveling safely at {speed} km/h"

print("\n--- Phase 3: Runtime Execution ---")

# Test 1: Within limits
result1 = drive_car(90)
print(f"Result: {result1}")

# Test 2: Over limits (The closure logic actively intercepts and mutates behavior)
result2 = drive_car(150)
print(f"Result: {result2}")