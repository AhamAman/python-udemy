from functools import reduce
import time

def separator(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Raw Data Setup
numbers = [1, 2, 3, 4, 5]
mixed_balances = [-10, 0, 45, 120, -5]

# =====================================================================
# 1. CORE TRANSFORMATIONS: map(), filter(), reduce()
# =====================================================================
separator("1. Core Functional Tools")

# map(func, iterable) -> Transforms each element without an explicit loop
squared_iterator = map(lambda x: x ** 2, numbers)
print(f"map() result (as list): {list(squared_iterator)}")

# filter(func, iterable) -> Extracts items that meet a boolean condition
positive_balances = filter(lambda x: x > 0, mixed_balances)
print(f"filter() result (as list): {list(positive_balances)}")

# reduce(func, iterable) -> Progressively reduces a collection down to a single value
# Computes: ((((1 * 2) * 3) * 4) * 5)
factorial = reduce(lambda x, y: x * y, numbers)
print(f"reduce() factorial result: {factorial}")


# =====================================================================
# 2. BOOLEAN EVALUATION: any() AND all()
# =====================================================================
separator("2. Short-Circuit Boolean Evaluation")

Flagged_transactions = [False, False, True, False]

# any() returns True if AT LEAST ONE item is truthy (Short-circuits immediately)
print(f"any() flagged transactions found? {any(Flagged_transactions)}")

# all() returns True only if EVERY item is truthy
scores = [90, 95, 88, 92]
print(f"all() scores above passing threshold (80)? {all(score > 80 for score in scores)}")


# =====================================================================
# 3. MATH AGGREGATIONS: sum(), max(), min()
# =====================================================================
separator("3. Specialized Mathematical Aggregations")

# Optimized C-level implementations instead of running manual accumulation trackers
print(f"sum() total: {sum(numbers)}")
print(f"max() value: {max(mixed_balances)}")
print(f"min() value: {min(mixed_balances)}")

# Complex item aggregation using the 'key' argument
users = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 34}]
oldest_user = max(users, key=lambda u: u["age"])
print(f"max(with key) oldest user object: {oldest_user}")


# =====================================================================
# 4. GENERATOR PIPELINES
# =====================================================================
separator("4. Memory-Efficient Generator Pipelines")

# Instead of loading large arrays into memory, stream transformations lazily
raw_logs = ["ERROR: System failure", "INFO: User login", "ERROR: DB timeout"]

# Step 1: Create a lazy stream that filters anomalies
error_stream = (log for log in raw_logs if log.startswith("ERROR"))

# Step 2: Create a downstream transformation that formats the filtered anomalies
formatted_stream = (error.upper() for error in error_stream)

print("Processing generator pipeline outputs lazily:")
for processed_log in formatted_stream:
    print(f"  Streamed Log: {processed_log}")


# =====================================================================
# 5. LOOPS VS. FUNCTIONAL PERFORMANCE COMPARISON
# =====================================================================
separator("5. Comparison: Loop vs Functional Performance")

large_range = range(1, 1_000_000)

# Approach A: Imperative Loop
start_loop = time.time()
loop_sum = 0
for num in large_range:
    if num % 2 == 0:
        loop_sum += num
loop_duration = time.time() - start_loop
print(f"Imperative Loop (for + if) Time:  {loop_duration:.5f} seconds")

# Approach B: Functional Pipeline
start_func = time.time()
# Done entirely at the C-layer via generator expression inside sum()
func_sum = sum(num for num in large_range if num % 2 == 0)
func_duration = time.time() - start_func
print(f"Functional Pipeline (sum) Time:   {func_duration:.5f} seconds")

separator("Execution Complete")