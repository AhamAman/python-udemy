"""
PRODUCTION DECORATOR PATTERNS SUITE

A single-file implementation of the 8 core architectural decorator use cases:
1. Logging      2. Timing        3. Authentication  4. Validation
5. Debugging   6. Access Control 7. Monitoring      8. Rate Limiting
"""

import time
import functools

# Mock Global States for Simulation
CURRENT_USER = {"username": "alice_dev", "role": "admin", "is_authenticated": True}
API_CALL_COUNTS = {}
LAST_CALL_TIMESTAMPS = {}

# ============================================================================
# 1. TIMING DECORATOR (Performance Benchmarking)
# ============================================================================
def time_performance(func):
    @functools.wraps(func)  # Preserves original function metadata (__name__, __doc__)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  [METRIC] '{func.__name__}' took {elapsed:.6f}s to execute.")
        return result
    return wrapper


# ============================================================================
# 2. LOGGING & DEBUGGING DECORATORS (Observability)
# ============================================================================
def log_lifecycle(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🪵 [LOG] Entering '{func.__name__}' | Args: {args} | Kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"🪵 [LOG] Exiting '{func.__name__}' successfully. Return type: {type(result)}")
            return result
        except Exception as e:
            print(f"🚨 [LOG] '{func.__name__}' crashed with exception: {str(e)}")
            raise
    return wrapper

def debug_inspect(func):
    """Injects comprehensive local evaluation stats for troubleshooting."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔍 [DEBUG] Inspecting Signature of '{func.__name__}'")
        print(f"   👉 Passed Positional Parameters: {args}")
        print(f"   👉 Passed Keyword Parameters: {kwargs}")
        result = func(*args, **kwargs)
        print(f"   👉 Evaluated Runtime Output: {result}")
        return result
    return wrapper


# ============================================================================
# 3. AUTHENTICATION & ACCESS CONTROL DECORATORS (Security)
# ============================================================================
def require_authentication(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not CURRENT_USER.get("is_authenticated"):
            raise PermissionError("🔒 [SECURITY] 401 Unauthorized: User authentication required.")
        print("🔒 [SECURITY] Authentication verified.")
        return func(*args, **kwargs)
    return wrapper

def verify_admin_role(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if CURRENT_USER.get("role") != "admin":
            raise PermissionError("🔒 [SECURITY] 403 Forbidden: Administrative privileges required.")
        print("🔒 [SECURITY] Access Control Authorization cleared.")
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# 4. VALIDATION DECORATOR (Data Integrity)
# ============================================================================
def validate_positive_integers(func):
    """Ensures input parameters strictly conform to domain logic bounds."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Scan positional args for anomalies
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"❌ [VALIDATION] Negative values not allowed. Found: {arg}")
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# 5. MONITORING & RATE LIMITING DECORATORS (Infrastructure Operations)
# ============================================================================
def monitor_traffic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Global counter tracking invocation metadata
        API_CALL_COUNTS[func.__name__] = API_CALL_COUNTS.get(func.__name__, 0) + 1
        print(f"📊 [MONITOR] Global Counter -> '{func.__name__}' has been executed {API_CALL_COUNTS[func.__name__]} times.")
        return func(*args, **kwargs)
    return wrapper

def limit_rate_1s(func):
    """Basic throttling protection layer preventing client flood loops."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        last_called = LAST_CALL_TIMESTAMPS.get(func.__name__, 0)
        current_time = time.time()
        
        if current_time - last_called < 1.0:
            print("⏳ [THROTTLE] Request dropped. Rate limit reached (Max 1 request per second).")
            return {"status": 429, "error": "Too Many Requests"}
            
        LAST_CALL_TIMESTAMPS[func.__name__] = current_time
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# TARGET ECOYSTEM: TESTING THE LAYERED ARCHITECTURE
# ============================================================================

@time_performance
@log_lifecycle
@validate_positive_integers
def process_financial_ledger(account_id, transfer_amount):
    """Simulates calculating ledger books."""
    time.sleep(0.1) # Simulate network database lag
    return f"Ledger updated for Account #{account_id}. Transferred: ${transfer_amount}"

@require_authentication
@verify_admin_role
@debug_inspect
def purge_system_cache():
    return "Cache system completely cleared."

@limit_rate_1s
@monitor_traffic
def fetch_public_status():
    return {"status": 200, "data": "Healthy"}


if __name__ == "__main__":
    print("=== PHASE 1: TESTING COMPREHENSIVE FINANCIAL PIPELINE ===")
    # Triggers: Time Performance -> Log Lifecycle -> Validation Checks
    ledger_output = process_financial_ledger(90210, 4500)
    print(f"Result: {ledger_output}\n")

    try:
        print("Triggering Validation Failure...")
        process_financial_ledger(90210, -500)
    except ValueError as e:
        print(f"Caught expected validation error: {e}\n")


    print("=== PHASE 2: TESTING SECURITY AND DEBUG LAYERS ===")
    # Triggers: Auth -> Admin Role -> Debug Verification
    security_output = purge_system_cache()
    print(f"Result: {security_output}\n")


    print("=== PHASE 3: TESTING INFRASTRUCTURE CONTROL (RATE LIMITS) ===")
    # First invocation should succeed
    print(f"Call 1: {fetch_public_status()}")
    # Instantaneous second invocation should hit rate limiting wrapper
    print(f"Call 2: {fetch_public_status()}")