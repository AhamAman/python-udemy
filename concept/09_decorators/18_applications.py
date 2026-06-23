import functools
import time
import random

# Mock Global Systems State
FEATURE_FLAGS = {"new_billing_engine": True}
USER_ROLES = {"user_123": "admin", "user_456": "guest"}
RATE_LIMIT_DB = {} # Tracks IP/User hit counts


# ==========================================
# 1. TIMING & METRICS COLLECTION DECORATOR
# ==========================================
def collect_metrics(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"[Metrics Engine] Starting execution tracker for '{func.__name__}'...")
        try:
            result = func(*args, **kwargs)
            status = "SUCCESS"
            return result
        except Exception as e:
            status = f"FAILED ({type(e).__name__})"
            raise e
        finally:
            duration = time.perf_counter() - start_time
            # Real world application: send this data to Prometheus, Datadog, or CloudWatch
            print(f"[Metrics Engine] Metric Sent -> Endpoint: {func.__name__} | Status: {status} | Latency: {duration:.6f}s")
    return wrapper


# ==========================================
# 2. AUTHENTICATION & ROLE AUTHORIZATION
# ==========================================
def require_role(required_role: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_id = kwargs.get("user_id")
            print(f"[Auth Security] Evaluating access control for User ID: {user_id}")
            
            # Authentication Check
            if not user_id or user_id not in USER_ROLES:
                print("[Auth Security] ❌ Failure: Unauthenticated Connection Attempted.")
                return {"status_code": 401, "message": "Unauthorized: Invalid Credentials"}
                
            # Authorization Check
            user_role = USER_ROLES[user_id]
            if user_role != required_role and user_role != "admin":
                print(f"[Auth Security] ❌ Failure: User role '{user_role}' lacks privilege '{required_role}'.")
                return {"status_code": 403, "message": "Forbidden: Insufficient Permissions"}
                
            print(f"[Auth Security] \u2705 Success: Cleared for role '{required_role}'.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ==========================================
# 3. FAULT-TOLERANT RETRY DECORATOR
# ==========================================
def retry_on_exception(max_attempts=3, backoff_delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    print(f"[Retry Engine] Network Hiccup: {e}. Attempt {attempts}/{max_attempts} failed. Retrying...")
                    if attempts >= max_attempts:
                        print("[Retry Engine] ❌ Failure: Resilience threshold exhausted.")
                        raise e
                    time.sleep(backoff_delay)
        return wrapper
    return decorator


# ==========================================
# 4. CONDITIONAL FEATURE FLAG DECORATOR
# ==========================================
def toggle_feature(flag_name: str, fallback_func):
    """If the feature flag is disabled, routes execution transparently to a legacy function."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            is_enabled = FEATURE_FLAGS.get(flag_name, False)
            if not is_enabled:
                print(f"[Feature Router] Flag '{flag_name}' is OFF. Rerouting request to fallback route...")
                return fallback_func(*args, **kwargs)
            print(f"[Feature Router] Flag '{flag_name}' is ON. Routing request to bleeding edge engine.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ==========================================
# 5. MOCK LEGACY/FALLBACK LOGIC
# ==========================================
def legacy_billing_processing(*args, **kwargs):
    print("   [Legacy Engine] Processing transaction via older, slower payment processor module.")
    return {"status_code": 200, "engine": "legacy", "transaction_id": "TX_OLD_999"}


# ==========================================
# 6. APPLICATION LAYER (THE API CONTROLLER)
# ==========================================

# We stack our bricks deliberately:
# 1. Collect performance metrics on EVERYTHING that happens.
# 2. Protect the gateway with Role Authorization.
# 3. Router logic determines if we call the new engine code.
# 4. If new code runs, apply network retry resilience loops.
@collect_metrics
@require_role(required_role="premium_user")
@toggle_feature(flag_name="new_billing_engine", fallback_func=legacy_billing_processing)
@retry_on_exception(max_attempts=2, backoff_delay=0.05)
def execute_billing_payout(user_id: str, amount: float, fail_simulation=False):
    """The cutting-edge, ultra-fast billing system endpoint."""
    print("   [Core Billing Engine] Executing advanced transaction algorithm...")
    
    if fail_simulation:
        # Simulate an intermittent third-party gateway network error
        raise ConnectionError("Stripe API Timeout Error")
        
    return {"status_code": 200, "engine": "next_gen", "payout_amount": amount}


# ==========================================
# 7. SIMULATING DECORATOR STACK RUNTIMES
# ==========================================
print("--- SCENARIO 1: Unauthenticated User Request ---")
response_1 = execute_billing_payout(user_id="anonymous_hacker", amount=500.0)
print(f"Final Client Payload: {response_1}\n")


print("--- SCENARIO 2: Authorized Guest User (Role Gate Block) ---")
# Guests don't have premium_user access, but admins do.
response_2 = execute_billing_payout(user_id="user_456", amount=500.0)
print(f"Final Client Payload: {response_2}\n")


print("--- SCENARIO 3: Admin Overrides Security, Flag Active, Network Flakes but Recovers ---")
# Admin triggers the pipeline, handles an internal network drop, and resolves cleanly
response_3 = execute_billing_payout(user_id="user_123", amount=1250.0, fail_simulation=True)
print(f"Final Client Payload: {response_3}\n")


print("--- SCENARIO 4: Turning Feature Flag Off Dynamic Check ---")
FEATURE_FLAGS["new_billing_engine"] = False # Simulate live remote configuration change
response_4 = execute_billing_payout(user_id="user_123", amount=1250.0)
print(f"Final Client Payload: {response_4}\n")