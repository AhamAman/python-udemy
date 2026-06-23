import itertools
import time

def separator(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# =====================================================================
# 1. CLASSIC NESTED FOR LOOPS
# =====================================================================
separator("1. Nested FOR Loops (Grid Coordinates)")

for row in range(1, 4):  # Outer Loop
    print(f"--- Starting Row {row} ---")
    for col in range(1, 4):  # Inner Loop
        print(f"  Coordinates: ({row}, {col})")


# =====================================================================
# 2. NESTED WHILE LOOPS
# =====================================================================
separator("2. Nested WHILE Loops")

row_tracker = 1
while row_tracker <= 3:  # Outer Loop
    col_tracker = 1  # CRITICAL: Reset inner variable for the new row cycle
    while col_tracker <= 3:  # Inner Loop
        print(f"  While-Grid: ({row_tracker}, {col_tracker})")
        col_tracker += 1
    row_tracker += 1


# =====================================================================
# 3. MIXED NESTING PATTERNS
# =====================================================================
separator("3. Mixed Nesting (FOR containing WHILE)")

checkout_lines = ["Line A", "Line B"]

for line in checkout_lines:  # Outer FOR loop
    print(f"Processing {line}...")
    customers_in_line = 3  # Dynamic count setup
    
    while customers_in_line > 0:  # Inner WHILE loop
        print(f"  Serving customer. {customers_in_line} remaining.")
        customers_in_line -= 1


# =====================================================================
# 4. TIME COMPLEXITY IMPACT (O(N) vs O(N²))
# =====================================================================
separator("4. Time Complexity Demonstration")

elements_count = 2000
dummy_list = list(range(elements_count))

print(f"Simulating operations with N = {elements_count} elements...")

# O(N) Linear Time Simulation
start_time = time.time()
for x in dummy_list:
    pass  # Imagine a quick, single operation here
linear_time = time.time() - start_time
print(f"-> Linear O(N) single loop took: {linear_time:.6f} seconds")

# O(N²) Quadratic Time Simulation
start_time = time.time()
for x in dummy_list[:500]:  # Capped at 500 to keep execution instant
    for y in dummy_list[:500]:
        pass  # Nested operation
quadratic_time = time.time() - start_time
print(f"-> Quadratic O(N²) nested loop (scaled to just 500x500) took: {quadratic_time:.6f} seconds")
print("Notice how steeply the time jumps when loops multiply execution scales!")


# =====================================================================
# 5. AVOIDING EXCESSIVE NESTING (Refactoring Strategies)
# =====================================================================
separator("5. Strategies to Avoid Deep Nesting")

# Strategy A: Flattening via itertools.product
print("Strategy A: Using itertools.product to eliminate visual indentation:")
for row, col in itertools.product(range(1, 4), range(1, 4)):
    print(f"  Flat Coordinates: ({row}, {col})")

# Strategy B: Functional Extraction
print("\nStrategy B: Extracting the inner loop logic into a distinct function:")

def process_columns_cleanly(row_index):
    """Encapsulates the inner loop operational duty."""
    for col_index in range(1, 4):
        print(f"  Isolated Function Coordinates: ({row_index}, {col_index})")

# The main execution code remains readable and shallow
for row_index in range(1, 4):
    print(f"--- Starting Clean Row {row_index} ---")
    process_columns_cleanly(row_index)

separator("Execution Complete")