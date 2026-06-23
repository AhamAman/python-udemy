import functools
import time

# ==========================================
# 1. THE MEMOIZATION DECORATOR
# ==========================================

def memoize(func):
    """
    A stateful decorator that caches function results based on arguments.
    Includes a basic cache invalidation method.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        # We use the 'args' tuple directly as the dictionary key
        if args in cache:
            return cache[args]
        
        # Compute and store if it's a cache miss
        result = func(*args)
        cache[args] = result
        return result

    # Expose the cache and an invalidation helper via function attributes
    wrapper.cache = cache
    
    def clear_cache():
        cache.clear()
        print(f"\n[Cache Invalidation] Cache cleared for '{func.__name__}'")
        
    wrapper.clear_cache = clear_cache
    return wrapper


# ==========================================
# 2. THE RECURSIVE TEST SUBSTANCES
# ==========================================

# Standard unoptimized recursive function
def raw_fibonacci(n):
    if n < 2:
        return n
    return raw_fibonacci(n - 1) + raw_fibonacci(n - 2)


# Optimized recursive function using our decorator
@memoize
def memoized_fibonacci(n):
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# ==========================================
# 3. PERFORMANCE AND TRADE-OFF BENCHMARKS
# ==========================================
print("--- Phase 1: Recursive Optimization & Performance Gains ---")

# Benchmark Raw Fibonacci (Exponential Time Complexity: O(2^n))
start_raw = time.time()
raw_val = raw_fibonacci(35)
duration_raw = time.time() - start_raw
print(f"[Raw] fib(35) = {raw_val} | Time taken: {duration_raw:.4f} seconds")

# Benchmark Memoized Fibonacci (Linear Time Complexity: O(n))
start_memo = time.time()
memo_val = memoized_fibonacci(35)
duration_memo = time.time() - start_memo
print(f"[Memoized] fib(35) = {memo_val} | Time taken: {duration_memo:.4f} seconds")

# Calculate performance multiplier
speedup = duration_raw / max(duration_memo, 1e-9)
print(f"\n>>> Performance Gain: Memoized version is roughly {speedup:.1f}x faster!")


print("\n--- Phase 2: Memory Trade-offs & Introspection ---")
# Introspect what the cache physically contains in memory
print(f"Total entries stored in memory cache: {len(memoized_fibonacci.cache)}")
print(f"Sample Cache Architecture: {dict(list(memoized_fibonacci.cache.items())[:5])}...")


print("\n--- Phase 3: Cache Invalidation ---")
# Call an upper number to populate cache further
_ = memoized_fibonacci(36)
print(f"Cache size before invalidation: {len(memoized_fibonacci.cache)}")

# Invalidate the cache to free up memory
memoized_fibonacci.clear_cache()
print(f"Cache size after invalidation: {len(memoized_fibonacci.cache)}")