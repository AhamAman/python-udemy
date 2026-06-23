"""
BUILDING A DECORATOR MANUALLY

This file demonstrates exactly how Python's '@' decorator syntax works 
under the hood by manually nesting, passing, wrapping, and executing functions.
"""

import time

# -----------------------------------------------------------------
# 1. The Decorator Function (The Factory)
# -----------------------------------------------------------------
def manual_timer_decorator(func):
    """
    Accepts a target function 'func' as an object.
    Returns a new wrapper function that encapsulates 'func'.
    """
    print(f"🛠️ [Factory] Decorator applied to '{func.__name__}'. Wrapper generated.")

    # This inner function captures 'func' from the outer scope (a Closure)
    def wrapper(*args, **kwargs):
        # STEP A: Add behavior BEFORE execution
        print(f"\n⏱️ [Wrapper] ---> Before execution of '{func.__name__}'")
        start_time = time.perf_counter()

        # STEP B: Call the original function and PRESERVE its return value
        print(f"🎯 [Wrapper] Executing original function '{func.__name__}' now...")
        result = func(*args, **kwargs) 

        # STEP C: Add behavior AFTER execution
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"⏱️ [Wrapper] <--- After execution. Elapsed: {execution_time:.6f}s")

        # STEP D: Return the preserved value back to the main thread
        return result

    # Return the executable wrapper object, passing it up to the caller
    return wrapper


# -----------------------------------------------------------------
# 2. The Target Function (The Payload)
# -----------------------------------------------------------------
def calculate_squares(limit):
    """A standard function that simulates heavy mathematical work."""
    print(f"   ⚡ [Core] Processing squares up to {limit}...")
    return [x**2 for x in range(limit)]


# ============================================================================
# TRACING EXECUTION STEP-BY-STEP
# ============================================================================

if __name__ == "__main__":
    print("--- 1. Verification of Raw Function ---")
    print(f"Original function object name: {calculate_squares.__name__}")
    # Running it normally without decorations
    raw_result = calculate_squares(3)
    print(f"Raw Result: {raw_result}")

    print("\n--- 2. Manually Decorating the Function ---")
    # We pass the function object into our factory.
    # 'decorated_squares' is now a reference to the inner 'wrapper' function.
    decorated_squares = manual_timer_decorator(calculate_squares)
    
    print(f"New object type: {type(decorated_squares)}")
    print(f"New object internal name property: {decorated_squares.__name__}")

    print("\n--- 3. Executing the Wrapped Pipeline ---")
    # When we call 'decorated_squares', we are actually invoking 'wrapper()'
    pipeline_result = decorated_squares(5)

    print("\n--- 4. Preserving the Return Value ---")
    print(f"Final Caller Received Data: {pipeline_result}")

    print("\n--- 5. What the '@' Syntax Actually Does ---")
    print("Writing:")
    print("@manual_timer_decorator\ndef my_func(): pass")
    print("\nIs exactly identical to writing:")
    print("my_func = manual_timer_decorator(my_func)")