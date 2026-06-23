import time

def separator(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# =====================================================================
# 1. REVERSE ITERATION WITH LISTS
# =====================================================================
separator("1. Reverse Iteration with Lists")

menu_items = ["Appetizer", "Main Course", "Dessert"]

print("Reading the menu backward using reversed():")
# The clean, Pythonic way
for item in reversed(menu_items):
    print(f"  - {item}")

print("\nWhat reversed() actually returns:")
print(f"  {reversed(menu_items)}")  # Prints the iterator memory object address


# =====================================================================
# 2. REVERSE ITERATION WITH RANGE()
# =====================================================================
separator("2. Reverse Iteration with Range")

# Method A: Using negative stride/step in range(start, stop, step)
# Remember: The 'stop' value is exclusive!
print("Method A: Counting down using range step (-1):")
for i in range(5, 0, -1):
    print(f"  T-minus {i}...")

# Method B: Wrapping a standard range in reversed()
print("\nMethod B: Wrapping a normal range in reversed():")
for i in reversed(range(1, 6)):
    print(f"  T-minus {i}...")


# =====================================================================
# 3. PERFORMANCE & MEMORY COMPARISON
# =====================================================================
separator("3. Performance Considerations")

# Creating a large dataset
large_dataset = list(range(10_000_000))

print("Case A: Slicing memory footprint [::-1]")
start_time = time.time()
# This creates a brand new copy of 10 million integers in memory!
for item in large_dataset[::-1]:
    break  # Just testing setup speed
slicing_duration = time.time() - start_time
print(f"  Slicing setup took: {slicing_duration:.6f} seconds (Creates a massive copy)")

print("\nCase B: Lazy execution using reversed()")
start_time = time.time()
# Instantly creates a tiny pointer object, using almost zero extra memory
for item in reversed(large_dataset):
    break  # Just testing setup speed
reversed_duration = time.time() - start_time
print(f"  reversed() setup took: {reversed_duration:.6f} seconds (O(1) memory pointer)")

separator("Execution Complete")