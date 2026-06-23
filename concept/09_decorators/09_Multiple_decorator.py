import functools

# ==========================================
# 1. DEFINE THE DECORATOR LAYERS
# ==========================================

def authenticate(func):
    print("[Decoration Time] Wrapping with @authenticate (Top Layer)")
    @functools.wraps(func)
    def auth_wrapper(*args, **kwargs):
        print("\n[Runtime - Layer 1] @authenticate checking permissions...")
        user_authenticated = kwargs.get("authenticated", False)
        if not user_authenticated:
            print("[Runtime - Layer 1] Access Denied!")
            return "401 Unauthorized"
        print("[Runtime - Layer 1] Access Granted.")
        return func(*args, **kwargs)
    return auth_wrapper


def log_action(func):
    print("[Decoration Time] Wrapping with @log_action (Middle Layer)")
    @functools.wraps(func)
    def log_wrapper(*args, **kwargs):
        print("[Runtime - Layer 2] @log_action logging start of transaction...")
        result = func(*args, **kwargs)
        print(f"[Runtime - Layer 2] @log_action logging success. Result: {result}")
        return result
    return log_wrapper


def validate_input(func):
    print("[Decoration Time] Wrapping with @validate_input (Bottom Layer)")
    @functools.wraps(func)
    def val_wrapper(*args, **kwargs):
        print("[Runtime - Layer 3] @validate_input checking parameters...")
        amount = kwargs.get("amount", 0)
        if amount <= 0:
            print("[Runtime - Layer 3] Validation Failed: Amount must be positive.")
            return "400 Bad Request"
        print("[Runtime - Layer 3] Validation Passed.")
        return func(*args, **kwargs)
    return val_wrapper

# ==========================================
# 2. STACKING THE DECORATORS
# ==========================================
print("--- PHASE 1: CODE LOADING / DECORATION ORDER ---")

# The order matters structurally. 
# We want to Authenticate -> Log the attempt -> Validate the clean data -> Execute.
@authenticate
@log_action
@validate_input
def transfer_funds(amount=0, authenticated=False):
    print(f"   [Target Function] Transferring ${amount} successfully!")
    return "200 OK"

# ==========================================
# 3. RUNNING THE CODE / RUNTIME EXECUTION
# ==========================================
print("\n--- PHASE 2: RUNTIME EXECUTION ORDER ---")

print("\n>>> Scenario A: Everything passes")
final_result_a = transfer_funds(amount=150, authenticated=True)
print(f"Final Output: {final_result_a}")

print("\n>>> Scenario B: Authentication fails early")
# Notice how execution stops at Layer 1. Middle and Bottom layers never run.
final_result_b = transfer_funds(amount=150, authenticated=False)
print(f"Final Output: {final_result_b}")

print("\n>>> Scenario C: Auth passes, Log happens, but Validation fails")
# Notice how Auth and Log run, but the target function is blocked by Layer 3.
final_result_c = transfer_funds(amount=-50, authenticated=True)
print(f"Final Output: {final_result_c}")