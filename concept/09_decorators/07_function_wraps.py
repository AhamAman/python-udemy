"""
DEMONSTRATING FUNCTOOLS.WRAPS

Features:
1. The metadata blindspot (broken __name__, __doc__, and __annotations__).
2. Fixing the identity using functools.wraps.
3. Accessing the original function using the __wrapped__ attribute.
"""

import functools

# -----------------------------------------------------------------
# Decorator A: Broken (Does NOT use functools.wraps)
# -----------------------------------------------------------------
def broken_decorator(func):
    def wrapper(*args, **kwargs):
        """Internal documentation for the broken wrapper."""
        return func(*args, **kwargs)
    return wrapper


# -----------------------------------------------------------------
# Decorator B: Correct (Uses functools.wraps)
# -----------------------------------------------------------------
def correct_decorator(func):
    # This copies the identity of 'func' directly over to 'wrapper'
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Internal documentation for the correct wrapper."""
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# TARGET FUNCTIONS
# ============================================================================

@broken_decorator
def fetch_analytics_data(user_id: int) -> dict:
    """Query high-priority data warehouse metrics for a user."""
    return {"metrics": "sampled"}


@correct_decorator
def process_payout(account_id: str) -> bool:
    """Disburse financial balances to external banking API nodes."""
    return True


# ============================================================================
# RUNTIME INSPECTION
# ============================================================================

if __name__ == "__main__":
    print("--- 1. The Broken Decorator Blindspot ---")
    # Calling it works, but the function's identity is completely overwritten
    print(f"Expected Name: 'fetch_analytics_data' | Actual Name: '{fetch_analytics_data.__name__}'")
    print(f"Expected Doc:  'Query high-priority...' | Actual Doc:  '{fetch_analytics_data.__doc__}'")
    print(f"Expected Hints: {{'user_id': <class 'int'>...}} | Actual Hints: {fetch_analytics_data.__annotations__}")

    print("\n--- 2. The Correct Decorator (With functools.wraps) ---")
    # Identity is flawlessly preserved
    print(f"Preserved Name: '{process_payout.__name__}'")
    print(f"Preserved Doc:  '{process_payout.__doc__.strip()}'")
    print(f"Preserved Hints: {process_payout.__annotations__}")

    print("\n--- 3. Bonus: Unwrapping the Function ---")
    # functools.wraps automatically adds a '__wrapped__' attribute.
    # This allows you to bypass the decorator entirely, which is invaluable for unit tests!
    print(f"Is 'process_payout' the wrapper? {process_payout.__name__}")
    
    original_unwrapped_func = process_payout.__wrapped__
    print(f"Extracted original function object: {original_unwrapped_func}")
    print(f"Bypassing decorator logic directly: {original_unwrapped_func('ACC-77')}")
    