# ==========================================
# 1. Basic Anonymous Lambda Mechanics
# ==========================================
print("--- Basic Lambda Collapse ---")

# Standard way:
def traditional_square(x):
    return x * x

# Lambda way (Assigned to a variable purely for illustration; don't do this in production)
lambda_square = lambda x: x * x

print(f"Traditional Output: {traditional_square(5)}")
print(f"Lambda Output:      {lambda_square(5)}")


# ==========================================
# 2. Key-Extraction Sorting Pattern (Production Grade)
# ==========================================
print("\n--- Key-Extraction Custom Sorting ---")

telemetry_nodes = [
    {"node_id": "Alpha", "latency": 45.2},
    {"node_id": "Beta",  "latency": 12.8},
    {"node_id": "Gamma", "latency": 92.1}
]

# We want to sort the dictionaries based on their inner latency metric values.
# The lambda takes a single dictionary element 'node' and extracts 'latency' instantly.
sorted_nodes = sorted(telemetry_nodes, key=lambda node: node["latency"])

print("Sorted Nodes by Latency (Low to High):")
for node in sorted_nodes:
    print(f"  {node}")


# ==========================================
# 3. Higher-Order Functional Programming Data Pipelines
# ==========================================
print("\n--- Map and Filter Data Pipelines ---")

raw_metrics = [12, 55, 30, 88, 5, 41]

# Pipeline Step A: Filter out all metrics below 40
# The lambda acts as a dynamic boolean gate
filtered_metrics = list(filter(lambda x: x >= 40, raw_metrics))
print(f"Filtered (>= 40): {filtered_metrics}")

# Pipeline Step B: Scale the remaining metrics by 10x using map
scaled_metrics = list(map(lambda x: x * 10, filtered_metrics))
print(f"Scaled (10x):     {scaled_metrics}")