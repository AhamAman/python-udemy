import csv
import json
from io import StringIO

# ==========================================
# 1. Raw Production Data Simulation
# ==========================================

# Mocking an upstream config environment dictionary
APP_CONFIG = {
    "ALLOWED_TIERS": {"PREMIUM", "ENTERPRISE", "STANDARD"},
    "MIN_REVENUE_THRESHOLD": 10.00
}

# Mocking a raw string buffer representing a messy CSV export file from disk
MOCK_CSV_FILE_BUFFER = """user_id,account_tier,gross_revenue,region_code
usr_901,premium,150.00, us-east 
usr_902,free,0.00,eu-west
usr_903,enterprise,4500.00,  us-west 
usr_904,premium,-25.00,ap-south
usr_905,legacy_tier,75.00,us-east
usr_906,standard,19.99, eu-central
"""

# ==========================================
# 2. Pipeline Execution Steps
# ==========================================
print("--- Initializing Production Data Transformation Pipeline ---")

# Step A: Safe File & CSV Ingestion (Simulating streaming from an open file descriptor)
csv_stream = csv.DictReader(StringIO(MOCK_CSV_FILE_BUFFER.strip()))

# Step B: Extraction & Sanitization (Using a generator expression for lazy stream processing)
# We strip trailing whitespaces from strings and cast financial data fields inline.
sanitized_records_generator = (
    {
        "uid": row["user_id"].strip().upper(),
        "tier": row["account_tier"].strip().upper(),
        "revenue": float(row["gross_revenue"]),
        "region": row["region_code"].strip().lower()
    }
    for row in csv_stream
)

# Step C: Gatekeeper Filtration (Applying enterprise configuration rules)
# We consume the generator stream, dropping records that fail config rules or contain anomalous math.
filtered_business_payloads = [
    record
    for record in sanitized_records_generator
    if record["tier"] in APP_CONFIG["ALLOWED_TIERS"]
    if record["revenue"] >= APP_CONFIG["MIN_REVENUE_THRESHOLD"]
]

print(f"Ingested and Filtered Production Records Count: {len(filtered_business_payloads)}")


# ==========================================
# 3. JSON Export Modeling (Working with JSON / APIs)
# ==========================================
print("\n--- Serializing Cleansed Payload to JSON API Layout ---")

# Task: Reshape records into a standardized API payload layout
# Adding structural nesting fields dynamically via a dictionary comprehension
api_response_body = {
    record["uid"]: {
        "account_profile": f"TIER::{record['tier']}",
        "billing_metrics": {"currency": "USD", "amount": record["revenue"]},
        "routing_zone": record["region"]
    }
    for record in filtered_business_payloads
}

# Pretty print the final constructed JSON structure
print(json.dumps(api_response_body, indent=2))


# ==========================================
# 4. Database Transaction Structuring
# ==========================================
print("\n--- Structuring Safe Database Inserts ---")

# Task: Map the finalized records into a frozen tuple format 
# matching a database schema target: (id, billing_tier, revenue_amount)
db_insert_batch_payload = [
    (item["uid"], item["tier"], item["revenue"])
    for item in filtered_business_payloads
]

print("Batched Array ready to pass into DB Driver ExecuteMany Engine:")
for record_tuple in db_insert_batch_payload:
    print(f"  Executing -> INSERT INTO account_ledger VALUES {record_tuple};")