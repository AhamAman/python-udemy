import time
from functools import wraps

# ==========================================
# 1. Base Decorator: Performance Timer
# ==========================================
def measure_execution_speed(func):
    """Calculates the exact execution duration of a function."""
    @wraps(func) # Preserves original function metadata natively
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Executes the wrapped target function object
        result = func(*args, **kwargs)
        
        duration = time.perf_counter() - start_time
        print(f"[METRIC] '{func.__name__}' execution speed: {duration:.6f}s")
        return result
    return wrapper


# ==========================================
# 2. Configurable Decorator (Accepts Arguments)
# ==========================================
def enforce_rbac_clearance(required_role):
    """Advanced Factory: Customizes authorization gates per endpoint."""
    def actual_decorator(func):
        @wraps(func)
        def wrapper(user_profile, *args, **kwargs):
            # Inspect input data structure dynamically
            if user_profile.get("role") != required_role:
                raise PermissionError(f"403 Forbidden: Missing {required_role} status.")
            return func(user_profile, *args, **kwargs)
        return wrapper
    return actual_decorator


# ==========================================
# 3. Production Deployment & Stacking Runs
# ==========================================
print("--- Initializing Backend Gateways ---")

# Mock User Records
active_admin = {"username": "alice_infra", "role": "admin"}
guest_user   = {"username": "bob_guest", "role": "guest"}

# Stacked Decorators: Order moves bottom-up.
# 1. RBAC verifies role. 2. Performance timer tracks total duration.
@measure_execution_speed
@enforce_rbac_clearance(required_role="admin")
def mutate_cloud_infrastructure(user):
    """Critical operational write vector."""
    print(f"  -> Successfully modifying data node cluster state for {user['username']}...")
    time.sleep(0.1) # Simulating internal latency
    return "Cluster state: RECYCLED"


# Execution Scenario A: Clear pass through both decorator gates
print("Execution Scenario A:")
print(f"Server Response: {mutate_cloud_infrastructure(active_admin)}\n")

# Execution Scenario B: Blocked instantly at the Authorization gate
print("Execution Scenario B:")
try:
    mutate_cloud_infrastructure(guest_user)
except PermissionError as err:
    print(f"Server Interception Result: {err}")


# ==========================================
# 4. Metadata Preservation Verification
# ==========================================
print("\n--- Metadata Shield Inspection ---")
# Verifying that functools.wraps successfully protected our introspection vectors
print(f"Inspected Function Name: '{mutate_cloud_infrastructure.__name__}'")
print(f"Inspected Docstring:     '{mutate_cloud_infrastructure.__doc__.strip()}'")