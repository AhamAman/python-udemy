import sys

# Simulated raw system event log lines stream (could represent a multi-gigabyte production file)
RAW_LOG_STREAM = [
    "2026-06-23 12:01:05 [INFO] Cluster node alpha online",
    "2026-06-23 12:02:11 [WARN] CPU threshold exceeded on node beta",
    "2026-06-23 12:03:45 [CRITICAL] Database write connection timeout",
    "2026-06-23 12:04:02 [INFO] Routine cleanup task completed",
]

# ==========================================
# 1. Eager vs Lazy Memory footprint Analysis
# ==========================================
print("--- 1. Object Memory Allocation Footprint ---")

# Numeric Range Scale Representation
scale = 100000

list_allocation = [num * 2 for num in range(scale)]
generator_state = (num * 2 for num in range(scale))

print(f"List Comprehension (Full Allocation) RAM size: {sys.getsizeof(list_allocation)} bytes")
print(f"Generator Expression (Lazy Blueprint) RAM size: {sys.getsizeof(generator_state)} bytes")
print("-> Note: Generator size remains fixed regardless of scale boundary.")


# ==========================================
# 2. Chaining Generator Pipelines
# ==========================================
print("\n--- 2. Chained Data Processing Pipelines ---")

# Step Pipeline A: Extract lines and filter out only high-severity entries
# No calculations are run yet; this simply registers an extraction blueprint
severity_filter_pipeline = (
    line for line in RAW_LOG_STREAM 
    if "[CRITICAL]" in line or "[WARN]" in line
)

# Step Pipeline B: Clean and transform the remaining elements from Pipeline A
# We wrap the downstream pipeline around our upstream source generator reference
sanitized_alert_pipeline = (
    line.strip().upper() 
    for line in severity_filter_pipeline
)

print("Pipeline initialized. Ready to pull records...")
print("---------------------------------------------")

# Step Pipeline C: Consume the pipeline elements sequentially on demand
# Elements move through the entire pipeline path single-file
for finalized_alert in sanitized_alert_pipeline:
    print(f"Dispatched Real-Time Alert Event Payload: {finalized_alert}")