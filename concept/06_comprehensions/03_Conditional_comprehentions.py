# Raw dataset: Network transaction records on a server cluster
NETWORK_TRANSACTIONS = [
    {"tx_id": "TX_101", "amount": 450.00, "status": "COMPLETED", "zone": "us-east"},
    {"tx_id": "TX_102", "amount": 1200.50, "status": "PENDING",   "zone": "eu-west"},
    {"tx_id": "TX_103", "amount": 50.00,   "status": "COMPLETED", "zone": "us-east"},
    {"tx_id": "TX_104", "amount": 9500.00, "status": "FAILED",    "zone": "ap-south"},
    {"tx_id": "TX_105", "amount": 3200.00, "status": "COMPLETED", "zone": "eu-west"},
]

# ==========================================
# 1. Basic Equality & Range Filtering
# ==========================================
print("--- 1. Basic Boundary Filtration ---")

# Target: High-value completed transactions (Amount > 1000 AND Status == COMPLETED)
high_value_completed = [
    tx["tx_id"] 
    for tx in NETWORK_TRANSACTIONS 
    if tx["status"] == "COMPLETED" and tx["amount"] > 1000.00
]
print(f"High-Value Completed IDs: {high_value_completed}")


# ==========================================
# 2. Membership Testing & Sequential Chaining
# ==========================================
print("\n--- 2. Advanced Membership Chaining ---")

DOMESTIC_ZONES = {"us-east", "us-west"}

# Target: Filter transactions that are inside domestic zones AND are NOT marked as FAILED
# Chaining two separate 'if' blocks replicates an implicit 'and' gatekeeper sequence
clean_domestic_txs = [
    tx["tx_id"]
    for tx in NETWORK_TRANSACTIONS
    if tx["zone"] in DOMESTIC_ZONES
    if not tx["status"] == "FAILED"
]
print(f"Clean Domestic Transaction IDs: {clean_domestic_txs}")


# ==========================================
# 3. Complex Filtering Logic vs. Readability
# ==========================================
print("\n--- 3. Handling Complex Selection Structures ---")

# Target: Identify high-risk transactions requiring fraud audits
# Complexity Rule: Audit if amount is extremely large (> 5000) OR if it failed in a non-US zone
audit_list = [
    tx
    for tx in NETWORK_TRANSACTIONS
    if tx["amount"] > 5000.00 or (tx["status"] == "FAILED" and tx["zone"] not in DOMESTIC_ZONES)
]

print("Flagged Fraud Audit Records:")
for record in audit_list:
    print(f"  {record}")