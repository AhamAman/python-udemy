import functools
import time

# ==========================================
# 1. functools.wraps (Metadata Protection)
# ==========================================
print("--- 1. Testing functools.wraps ---")

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_decorator(func):
    @functools.wraps(func)  # Links wrapper metadata back to the original function
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def calculate_tax(amount):
    """Calculates standard state tax."""
    return amount * 0.08

@good_decorator
def calculate_shipping(weight):
    """Calculates standard freight shipping cost."""
    return weight * 1.2

print(f"Bad Decorator  -> Name: {calculate_tax.__name__:<15} | Doc: {calculate_tax.__doc__}")
print(f"Good Decorator -> Name: {calculate_shipping.__name__:<15} | Doc: {calculate_shipping.__doc__}")


# ==========================================
# 2. functools.partial (Argument Pre-binding)
# ==========================================
print("\n--- 2. Testing functools.partial ---")

def send_api_request(endpoint, timeout, payload):
    return f"Sending to /{endpoint} (Timeout: {timeout}s) with payload: {payload}"

# Real-world application: Create a specialized utility with arguments pre-frozen
# We fix 'endpoint' and 'timeout', leaving only 'payload' to be supplied later.
secure_fast_post = functools.partial(send_api_request, endpoint="v1/secure-pay", timeout=2)

print(secure_fast_post(payload={"amount": 250}))
print(secure_fast_post(payload={"amount": 400}))


# ==========================================
# 3. functools.cache vs. functools.lru_cache
# ==========================================
print("\n--- 3. Testing Caching Mechanisms ---")

# Unbounded Cache: Infinite growth. Great for static, predictable lookups.
@functools.cache
def lookup_db_config(setting_name):
    print(f"   [DB Query] Fetching raw data for: '{setting_name}'...")
    return f"Value_For_{setting_name}"

# Bounded Cache: Discards the Least Recently Used entries once it hits 'maxsize'.
# Great for long-running servers keeping memory consumption predictable.
@functools.lru_cache(maxsize=3)
def process_user_avatar(user_id):
    print(f"   [Heavy Processing] Rendering avatar image for User #{user_id}...")
    return f"Buffer_Data_User_{user_id}"

print("\n>>> Testing Unbounded @functools.cache:")
lookup_db_config("host")
lookup_db_config("host")  # Instant cache hit

print("\n>>> Testing Bounded @functools.lru_cache (Maxsize=3):")
process_user_avatar(1)
process_user_avatar(2)
process_user_avatar(3)

print("   Calling User #1 again to keep them 'Recently Used'...")
process_user_avatar(1)  # Cache hit, updates usage recency

print("   Adding User #4 (Forces eviction of User #2, since #1 was touched recently)...")
process_user_avatar(4)  # Eviction triggered here

print("\n   Checking if User #2 is still cached:")
process_user_avatar(2)  # Cache miss! Re-runs the print statement

# Inspect cache status metrics at runtime
print(f"\nCache Info for Avatar Processor: {process_user_avatar.cache_info()}")