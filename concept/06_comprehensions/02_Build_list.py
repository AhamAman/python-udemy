# ==========================================
# 1. Consuming Sequences (Ranges, Strings, Tuples)
# ==========================================
print("--- 1. Mapping Sequences ---")

# Numeric Range -> Creating derived squares
derived_squares = [num ** 2 for num in range(1, 6)]
print(f"From Range (Squares):  {derived_squares}")

# String -> Extracting character array with case translation
raw_firmware_id = "fw-7A9"
character_matrix = [char.upper() for char in raw_firmware_id]
print(f"From String (Matrix):  {character_matrix}")

# Tuple -> Converting frozen coordinates to floating metrics
frozen_gps_coords = (18.5204, 73.8567, 560)
floated_metrics = [float(coord) * 1.05 for coord in frozen_gps_coords]
print(f"From Tuple (Metrics):  {floated_metrics}")


# ==========================================
# 2. Consuming Unordered Collections (Sets, Dicts)
# ==========================================
print("\n--- 2. Mapping Unordered Collections ---")

# Set -> Converting unique, unordered IDs into a sorted list tracking sequence
unique_worker_ids = {"worker_9", "worker_2", "worker_9", "worker_5"} # Note duplicated 'worker_9'
ordered_workers = [worker.replace("_", "-") for worker in unique_worker_ids]
print(f"From Set (De-duplicated): {ordered_workers}")

# Dictionary -> Mapping different structural layers
cluster_nodes_ips = {
    "node_alpha": "10.0.0.1",
    "node_beta":  "10.0.0.2",
    "node_gamma": "10.0.0.3"
}

# Extraction Scenario A: Mapping dict keys
extracted_node_names = [name.upper() for name in cluster_nodes_ips]
print(f"From Dict (Keys Only):    {extracted_node_names}")

# Extraction Scenario B: Mapping dict values
extracted_network_ips = [f"HTTPS://{ip}" for ip in cluster_nodes_ips.values()]
print(f"From Dict (Values Only):  {extracted_network_ips}")

# Extraction Scenario C: Unpacking complete key-value pairs (Items)
formatted_inventory = [f"{key.upper()} -> {ip}" for key, ip in cluster_nodes_ips.items()]
print(f"From Dict (Full Unpack):  {formatted_inventory}")