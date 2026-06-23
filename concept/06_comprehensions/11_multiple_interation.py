# Upstream telemetry tracking states
SERVER_NAMES = ["node-alpha", "node-beta", "node-gamma"]
CPU_LOADS    = [42.1, 88.7, 15.3]
MEM_LOADS    = [60.2, 91.4, 34.0]

# ==========================================
# 1. Parallel Iteration via zip()
# ==========================================
print("--- 1. Synchronized Parallel Mapping ---")

# Task: Zip three separate metrics lists together to form unified dictionary payloads
# We unpack the zipped tuple cleanly directly inside the loop context declaration
cluster_manifest = [
    {"name": name, "cpu": cpu, "mem": mem}
    for name, cpu, mem in zip(SERVER_NAMES, CPU_LOADS, MEM_LOADS, strict=True)
]

print("Assembled Cluster Matrix:")
for record in cluster_manifest:
    print(f"  {record}")


# ==========================================
# 2. Positional Tracking via enumerate()
# ==========================================
print("\n--- 2. Index-Driven Transformation ---")

# Task: Standardize system names by injecting their physical rank sequence index
# Enumerate yields (index, item) tuples sequentially
ranked_nodes = [
    f"RANK-0{index}::{name.upper()}"
    for index, name in enumerate(SERVER_NAMES, start=1)
]
print(f"Ranked System Manifest: {ranked_nodes}")


# ==========================================
# 3. Data Merging / Map Reindexing
# ==========================================
print("\n--- 3. Merging Disparate Map Datasets ---")

NETWORK_IPS  = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

# Task: Construct a hot-lookup dictionary mapping names directly to network routing strings
dns_lookup_table = {
    name: f"https://{ip}:8080"
    for name, ip in zip(SERVER_NAMES, NETWORK_IPS)
}
print(f"Compiled Lookup Map: {dns_lookup_table}")


# ==========================================
# 4. Strict Safety Enforcement Gates
# ==========================================
print("\n--- 4. Mismatched Dataset Guardrail Verification ---")

MALFORMED_LOADS_ARRAY = [42.1, 88.7] # Missing node-gamma metric entry completely

try:
    # strict=True intercepts the error before it maps half-completed records into production
    corrupted_pipeline = [
        (name, load)
        for name, load in zip(SERVER_NAMES, MALFORMED_LOADS_ARRAY, strict=True)
    ]
except ValueError as err:
    print(f"Caught expected Data Alignment Error: {err}")
    print("-> Guardrail success: strict=True blocked silent compilation of a corrupted array.")