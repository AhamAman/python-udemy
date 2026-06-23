"""
UNDERSTANDING *args AND **kwargs IN DECORATORS

Demonstrating:
1. Tuple packing with *args
2. Dictionary packing with **kwargs
3. Runtime inspection and debugging of forwarded parameters
4. Total structural wrapper flexibility
"""

import functools

def structural_inspector(func):
    """A decorator that intercepts, inspects, and forwards any arbitrary signature."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # -------------------------------------------------------------
        # DEBUGGING LAYER: Inspecting the packed collections
        # -------------------------------------------------------------
        print(f"\n🔍 [Inspector] Intercepted invocation for: '{func.__name__}'")
        print(f"   ℹ️ Type of 'args':   {type(args).__name__} | Contents: {args}")
        print(f"   ℹ️ Type of 'kwargs': {type(kwargs).__name__} | Contents: {kwargs}")
        
        # We can structurally read or modify these values before forwarding!
        if args:
            print(f"   👉 First positional argument detected: {args[0]}")
        if "timeout" in kwargs:
            print(f"   ⚠️ Warning: Custom timeout configuration detected ({kwargs['timeout']}s)")

        # -------------------------------------------------------------
        # FORWARDING LAYER: Unpacking back into raw arguments
        # -------------------------------------------------------------
        # The '*' unpacks the tuple; the '**' unpacks the dictionary.
        # This mirrors the exact shape the caller provided.
        result = func(*args, **kwargs)
        
        return result

    return wrapper


# ============================================================================
# TARGET ECOSYSTEM: SHOWCASED WITH UNKNOWN SIGNATURES
# ============================================================================

@structural_inspector
def connect_database(host, port, timeout=30):
    """Accepts fixed positionals and an explicit keyword argument."""
    return f"Connected to {host}:{port} (Timeout: {timeout}s)"

@structural_inspector
def commit_telemetry(*metrics, **tags):
    """Accepts completely variable positional streams and variable keyword tags."""
    return f"Processed {len(metrics)} metrics with tags: {list(tags.keys())}"


# ============================================================================
# RUNTIME VERIFICATION
# ============================================================================

if __name__ == "__main__":
    print("--- Scenario A: Fixed Parameters Mixed With Defaults ---")
    # 10.0.0.1 and 5432 pack into 'args'. timeout=5 packs into 'kwargs'.
    db_status = connect_database("10.0.0.1", 5432, timeout=5)
    print(f"📡 Result: {db_status}")

    print("\n--- Scenario B: Purely Dynamic Streams ---")
    # All raw integers pack into 'args'. Named keys pack into 'kwargs'.
    telemetry_status = commit_telemetry(
        45, 89, 102, 11, 
        env="production", 
        region="us-west", 
        service="auth"
    )
    print(f"📡 Result: {telemetry_status}")

    