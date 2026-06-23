# Raw dataset: Active worker clusters with their hardware node IDs
CLUSTER_INVENTORY = [
    {"node_id": "alpha_01", "ip": "10.0.0.1", "active_cores": 8},
    {"node_id": "beta_02",  "ip": "10.0.0.2", "active_cores": 16},
    {"node_id": "gamma_03", "ip": "10.0.0.3", "active_cores": 4},
]

# ==========================================
# 1. Building a Lookup Table from an Iterable
# ==========================================
print("--- 1. Generating Index Lookup Table ---")

# Target: Map node_id strings directly to their nested dictionary payloads.
# This yields an O(1) index map out of an O(n) raw list configuration.
node_lookup_table = {node["node_id"]: node for node in CLUSTER_INVENTORY}

print(f"Direct Lookup Result for 'beta_02':\n  {node_lookup_table['beta_02']}")


# ==========================================
# 2. Transforming Keys and Values Independent Matrix
# ==========================================
print("\n--- 2. Independent Syntactic Transforms ---")

BASE_METRICS = {"node_01": 45, "node_02": 92, "node_03": 14}

# Scenario A: Transforming Keys Only (Normalizing casing and prefixes)
normalized_keys = {k.upper().replace("_", "-"): v for k, v in BASE_METRICS.items()}
print(f"Transformed Keys Map:   {normalized_keys}")

# Scenario B: Transforming Values Only (Scaling performance metrics by 100x)
scaled_values = {k: v * 100 for k, v in BASE_METRICS.items()}
print(f"Transformed Values Map: {scaled_values}")


# ==========================================
# 3. Conditional Dictionary Creation
# ==========================================
print("\n--- 3. Tail-End Conditional Filtering ---")

# Target: Filter our lookup base, keeping only nodes with metrics > 30
filtered_nodes = {k: v for k, v in BASE_METRICS.items() if v > 30}
print(f"Filtered Dictionary:    {filtered_nodes}")


# ==========================================
# 4. Bidirectional Dictionary Inversion
# ==========================================
print("\n--- 4. Structural Map Inversion ---")

dns_routing_map = {"app.internal": "10.0.0.5", "db.internal": "10.0.0.9"}

# Target: Flip keys and values completely around
# Inversion Rule: Swap the assignment positions before the colon
inverted_routing_map = {ip: host for host, ip in dns_routing_map.items()}
print(f"Inverted Routing Map:   {inverted_routing_map}")
# We can now look up the domain name using the IP string address instantly!
print(f"Lookup for '10.0.0.9':  {inverted_routing_map['10.0.0.9']}")