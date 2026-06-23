# ==========================================
# 1. The Dangerous Trap (The Anti-Pattern)
# ==========================================
print("--- The Mutable Default Trap ---")

def append_to_broken_list(value, current_items=[]):
    """
    DANGEROUS: 'current_items' points to a single mutable list instance
    allocated at definition time.
    """
    current_items.append(value)
    return current_items

# First call: works as expected
run_one = append_to_broken_list("Transaction_A")
print(f"Run 1 Output: {run_one}")

# Second call: Expecting an empty list fallback, but the old list resurfaces!
run_two = append_to_broken_list("Transaction_B")
print(f"Run 2 Output: {run_two}  <- Bug! Data has leaked from Run 1.")

# Peeking under the hood at the shared function memory cache
print(f"Internal function memory cache holds: {append_to_broken_list.__defaults__}")


# ==========================================
# 2. The Refactored Solution (The Production Pattern)
# ==========================================
print("\n--- The Safe None Sentinel Pattern ---")

def append_to_safe_list(value, current_items=None):
    """
    SAFE: Uses an immutable sentinel 'None'.
    A fresh container is allocated on the stack frame during execution time.
    """
    if current_items is None:
        current_items = [] # Fresh allocation per call
        
    current_items.append(value)
    return current_items

# Every call now remains cleanly isolated
safe_run_one = append_to_safe_list("Payload_A")
print(f"Safe Run 1: {safe_run_one}")

safe_run_two = append_to_safe_list("Payload_B")
print(f"Safe Run 2: {safe_run_two}  <- Completely clean and isolated.")