"""
PRESERVING FUNCTION BEHAVIOR IN DECORATORS

Demonstrating:
1. Universal argument capturing via *args and **kwargs.
2. Unpacking and forwarding parameters transparently.
3. Capturing and returning exact payload results.
"""

import functools

def transparent_proxy_decorator(func):
    """A perfectly transparent decorator template."""
    
    # Copy original metadata (__name__, __doc__, __annotations__) to the wrapper
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n⚡ [Proxy] Intercepted call to '{func.__name__}'")
        print(f"   📥 Packed positional args (tuple): {args}")
        print(f"   📥 Packed keyword args (dict):   {kwargs}")
        
        # 1. Forwarding arguments seamlessly using unpacking syntax
        # This converts the tuple and dict back into raw positional/keyword pairs
        result = func(*args, **kwargs)
        
        print(f"   📤 Captured internal result: {result} (Type: {type(result).__name__})")
        
        # 2. Returning the exact unmodified data back to the caller
        return result
        
    return wrapper


# ============================================================================
# TARGET ECOSYSTEM: THREE COMPLETELY DIFFERENT SIGNATURES
# ============================================================================

@transparent_proxy_decorator
def process_no_args():
    """Takes nothing, returns a static confirmation string."""
    return "Status Nominal"

@transparent_proxy_decorator
def compute_volume(length, width, height=1):
    """Takes mixed positional and optional keyword arguments, returns an int."""
    return length * width * height

@transparent_proxy_decorator
def generate_user_profile(user_id, **metadata):
    """Takes an explicit positional arg and arbitrary keywords, returns a dict."""
    profile = {"id": user_id}
    profile.update(metadata)
    return profile


# ============================================================================
# RUNTIME VERIFICATION
# ============================================================================

if __name__ == "__main__":
    print("--- Case 1: Zero Arguments ---")
    res1 = process_no_args()
    print(f"👉 Main Caller Received: '{res1}'")

    print("\n--- Case 2: Mixed Positional & Default Keywords ---")
    # Passing 5 and 10 positionally, and explicitly overriding height via keyword
    res2 = compute_volume(5, 10, height=3)
    print(f"👉 Main Caller Received: {res2}")

    print("\n--- Case 3: Arbitrary Dynamic Keywords ---")
    # Passing dynamic attributes that the decorator has never seen before
    res3 = generate_user_profile(
        42, 
        username="matrix_dev", 
        role="engineer", 
        clearance="Level-5"
    )
    print(f"👉 Main Caller Received: {res3}")
    
    print("\n--- Case 4: Metadata Integrity Verification ---")
    # Verifying that the docstring and name properties are preserved
    print(f"Function Name: {compute_volume.__name__}")
    print(f"Docstring:     {compute_volume.__doc__.strip()}")