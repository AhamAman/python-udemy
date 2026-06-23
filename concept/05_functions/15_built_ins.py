from functools import reduce

# Raw production logs: Server cluster state telemetry
CLUSTER_LOGS = [
    {"node": "us-east-01", "status": "ONLINE",  "cpu_load": 42},
    {"node": "us-east-02", "status": "ONLINE",  "cpu_load": 88},
    {"node": "eu-west-01", "status": "OFFLINE", "cpu_load": 0},
    {"node": "us-west-01", "status": "ONLINE",  "cpu_load": 95},
    {"node": "ap-south-01", "status": "ONLINE", "cpu_load": 15},
]

# ==========================================
# 1. Custom Functional Callback Primitives
# ==========================================
def isolate_active_nodes(node_record):
    """Boolean predicate function for filtering."""
    return node_record["status"] == "ONLINE"

def extract_cpu_load(node_record):
    """Transformation function for mapping."""
    return node_record["cpu_load"]

def accumulate_total_workload(running_sum, current_load):
    """Accumulator function for reducing."""
    return running_sum + current_load


# ==========================================
# 2. Assembling the Pipeline Stream
# ==========================================
print("--- Pipeline Execution Stream ---")

# Step A: Filter out offline nodes
active_stream = filter(isolate_active_nodes, CLUSTER_LOGS)

# Step B: Map / Extract raw numerical values from dictionaries
load_stream = map(extract_cpu_load, active_stream)

# NOTE: Up to this point, load_stream is a lazy iterator. No math has happened yet.
print(f"Lazy Stream Proxy Object Reference: {load_stream}")

# Step C: Fully consume the streams to calculate total cumulative workload
total_load = reduce(accumulate_total_workload, load_stream, 0)
print(f"Pipeline Result -> Total Cumulative Active CPU Load: {total_load}%")


# ==========================================
# 3. System Invariants Verification (any / all)
# ==========================================
print("\n--- System Invariant Verification ---")

# Invariant 1: Is our cluster in critical alert state? (Any node > 90% load?)
# Generates a quick inline generator stream to evaluate conditions
is_critical_alert = any(node["cpu_load"] > 90 for node in CLUSTER_LOGS)
print(f"Is critical system alert triggered? {is_critical_alert}")

# Invariant 2: Are all systems completely online?
is_entire_fleet_healthy = all(node["status"] == "ONLINE" for node in CLUSTER_LOGS)
print(f"Is entire server fleet online?       {is_entire_fleet_healthy}")


# ==========================================
# 4. Custom Architectural Sorting Engine
# ==========================================
print("\n--- Custom Key Weight Sorting ---")

# Sort nodes from highest load to lowest load using an inline anonymous lambda callback
sorted_by_utilization = sorted(
    CLUSTER_LOGS, 
    key=lambda node: node["cpu_load"], 
    reverse=True
)

print("Fleet Rankings (Highest Load to Lowest):")
for node in sorted_by_utilization:
    print(f"  Node: {node['node']} -> {node['cpu_load']}% Load")