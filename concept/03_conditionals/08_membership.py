# ==========================================
# 1. Basic Membership in Action
# ==========================================
print("--- Text Substring Checks ---")
quote = "Keep things first principle exploring causality."

# Strings look for contiguous substring matches
print(f"Is 'causality' in quote?   {'causality' in quote}")
print(f"Is 'veteran' not in quote? {'veteran' not in quote}")


# ==========================================
# 2. Sequential vs Hash Layout Mechanics
# ==========================================
print("\n--- Collection Target Discrepancies ---")
user_profile = {"id": 99, "username": "alpha_dev", "role": "admin"}

# Dictionary membership checks KEYS, not values!
print(f"Is 'username' in user_profile? {'username' in user_profile}") # True
print(f"Is 'admin' in user_profile?    {'admin' in user_profile}")    # False


# ==========================================
# 3. High-Scale Performance Benchmark
# ==========================================
print("\n--- Empirical Performance Speed Test ---")
import time

# Create a sequence of 10 million integers
limit = 10_000_000
target_num = 9_999_999 # Placed right at the end to force worst-case scenario

search_list = list(range(limit))
search_set = set(range(limit))

# Benchmark List Execution (Linear Search O(n))
start_time = time.perf_counter()
is_in_list = target_num in search_list
list_duration = time.perf_counter() - start_time
print(f"List Search: Found={is_in_list} | Took: {list_duration:.6f} seconds")

# Benchmark Set Execution (Hash Lookup O(1))
start_time = time.perf_counter()
is_in_set = target_num in search_set
set_duration = time.perf_counter() - start_time
print(f"Set Search:  Found={is_in_set}  | Took: {set_duration:.6f} seconds")

print(f"\nResult: Set lookup was roughly {list_duration / set_duration:.1f}x faster than the list!")