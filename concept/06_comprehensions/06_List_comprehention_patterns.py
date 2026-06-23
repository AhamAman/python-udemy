# Simulated raw response payload fetched from a multi-regional cloud API cluster
RAW_API_RESPONSE = {
    "status": "200 OK",
    "metadata": {"batch_id": 90114},
    "regions": [
        {
            "cluster_name": "us-east",
            "nodes": [
                {"node_id": " NODE-01 ", "load": 42.5, "status": "active"},
                {"node_id": "node-02 ", "load": -99.0, "status": "maintenance"}, # Invalid/Anomaly load
                {"node_id": "NODE-03", "load": 88.1, "status": "active"}
            ]
        },
        {
            "cluster_name": "eu-west",
            "nodes": [
                {"node_id": "node-04", "load": 12.0, "status": "active"},
                None, # Corrupted or null node reference slot
                {"node_id": "  NODE-05", "load": 94.7, "status": "active"}
            ]
        }
    ]
}

# ==========================================
# 1. Structural Flattening & Invariant Guarding
# ==========================================
print("--- 1. Flattening and Guarding Phase ---")

# Task: Unroll the nested regions/nodes layout into a single flat list of node records,
# simultaneously guarding our pipeline against null pointer elements (None).
# Sequential Rule: Outer loop first, followed by inner loop, capped with trailing filter.
all_valid_nodes = [
    node
    for region in RAW_API_RESPONSE["regions"]
    for node in region["nodes"]
    if node is not None # Structural guard against corrupt empty slots
]

print(f"Flattened and Guarded Node Array Size: {len(all_valid_nodes)}")


# ==========================================
# 2. Data Cleaning, Filtering, and Normalization
# ==========================================
print("\n--- 2. Data Cleaning and Sanitization Phase ---")

# Task: Standardize our metrics data.
# 1. Strip whitespaces and force casing on 'node_id' (Data Normalization).
# 2. Filter out anomalous metrics where 'load' falls below 0.0 (Data Cleaning).
sanitized_nodes = [
    {
        "node_id": node["node_id"].strip().upper(),
        "load": node["load"],
        "status": node["status"]
    }
    for node in all_valid_nodes
    if node["load"] >= 0.0 # Gatekeeper filter catches and eliminates 'node-02' (-99.0)
]

print("Sanitized Performance Matrix Profiles:")
for node in sanitized_nodes:
    print(f"  {node}")


# ==========================================
# 3. Field Extraction & Conditional Replacements
# ==========================================
print("\n--- 3. Field Extraction and Ternary Labeling ---")

# Task: 
# 1. Project a simple array of just the normalized load values (Field Extraction).
# 2. Apply a mathematical calculation: Square the loads to calculate weight vectors (Squaring).
# 3. Create a warning flag sequence using an inline front-end conditional expression (Conditional Replacement).

extracted_loads = [node["load"] for node in sanitized_nodes]
squared_loads   = [round(load ** 2, 2) for load in extracted_loads]

# Applying a front-end ternary operator to change values without dropping records
alert_manifest = [
    "FLAG_CRITICAL" if load > 90.0 else "FLAG_STABLE"
    for load in extracted_loads
]

print(f"Extracted Raw Loads:  {extracted_loads}")
print(f"Squared Weight Values: {squared_loads}")
print(f"Generated Alert State Manifest: {alert_manifest}")