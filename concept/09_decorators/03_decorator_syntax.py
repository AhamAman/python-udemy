"""
DECORATOR SYNTAX EXPOSED

Demonstrating:
1. The '@' syntax expansion.
2. Decoration-time execution vs Runtime execution.
3. The execution order of stacked decorators.
"""

def decorator_top(func):
    print(f"🛠️  [Decoration Time] 'decorator_top' is wrapping '{func.__name__}'")
    def wrapper_top(*args, **kwargs):
        print("🟢 [Runtime] Entering 'decorator_top' wrapper")
        result = func(*args, **kwargs)
        print("🔴 [Runtime] Exiting 'decorator_top' wrapper")
        return result
    return wrapper_top

def decorator_bottom(func):
    print(f"🛠️  [Decoration Time] 'decorator_bottom' is wrapping '{func.__name__}'")
    def wrapper_bottom(*args, **kwargs):
        print("  🔵 [Runtime] Entering 'decorator_bottom' wrapper")
        result = func(*args, **kwargs)
        print("  🟠 [Runtime] Exiting 'decorator_bottom' wrapper")
        return result
    return wrapper_bottom


# ============================================================================
# PHASE 1: DECORATION TIME (Happens immediately during parsing)
# ============================================================================
print("--- Phase 1: Parsing and Decorating Functions ---")

@decorator_top
@decorator_bottom
def core_payload(data):
    print(f"    🎯 [Runtime] Core Payload running with data: '{data}'")
    return data.upper()

# ----------------------------------------------------------------------------
# UNDER THE HOOD EXPANSION ARCHITECTURE
# 
# Writing the above code is EXACTLY equivalent to Python executing this:
#
# core_payload = decorator_top(decorator_bottom(core_payload))
#
# Notice why it goes bottom-up: 'decorator_bottom' must run first to wrap 
# the core function, then 'decorator_top' wraps the resulting wrapper!
# ----------------------------------------------------------------------------


# ============================================================================
# PHASE 2: RUNTIME (Happens when invoked)
# ============================================================================
print("\n--- Phase 2: Explicit Invocation at Runtime ---")

print("Calling core_payload()...")
final_output = core_payload("hello syntax")

print(f"\nFinal Result received by caller: '{final_output}'")