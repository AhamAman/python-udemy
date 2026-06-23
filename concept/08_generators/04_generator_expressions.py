import sys

# A structural representation of a high-volume data scale
DATA_SCALE = 100_000

# ==========================================
# 1. Memory Footprint Contrast
# ==========================================
print("--- 1. Memory Space Allocation Profiling ---")

# Eager evaluation: Builds the entire list structure in RAM instantly
eager_list = [num * 2 for num in range(DATA_SCALE)]

# Lazy evaluation: Only stores the structural instruction recipe
lazy_gen  = (num * 2 for num in range(DATA_SCALE))

print(f"List Comprehension Array Size: {sys.getsizeof(eager_list)} bytes")
print(f"Generator Expression Object Size: {sys.getsizeof(lazy_gen)} bytes")
print("-> Mechanical Fact: The generator size remains fixed regardless of scale.")


# ==========================================
# 2. Lazy Evaluation & The Pipeline Effect
# ==========================================
print("\n--- 2. Tracking Lazy Pipeline Execution ---")

RAW_METRICS = ["system-load:45", "system-load:92", "system-load:12"]

# Step Pipeline A: String token extraction blueprint (Nothing is evaluated yet)
extraction_pipeline = (line.split(":")[1] for line in RAW_METRICS)

# Step Pipeline B: Integer casting blueprint wrapped around Pipeline A
casting_pipeline = (int(value) for value in extraction_pipeline)

# Step Pipeline C: Boundary filter blueprint wrapped around Pipeline B
filter_pipeline = (val for val in casting_pipeline if val > 40)

print(f"Pipeline Object Reference State: {filter_pipeline}")
print("Ready to pull data from the stream...")
print("---------------------------------------------")

# The data elements travel down the entire pipeline single-file on demand
for passed_metric in filter_pipeline:
    print(f"Consumer Intercepted Sanitized Value: {passed_metric}")