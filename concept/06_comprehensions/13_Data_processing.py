# Raw incoming data stream segment representing a messy, un-sanitized dataset export
RAW_LOGDATA_STREAM = [
    "USER_ID ; TIER ; MONTHLY_REVENUE ; STATUS",
    "usr_201  ; premium ; 45.50  ; active",
    "usr_202  ; free    ; 0.00   ; active",
    "  ;   ;   ;  ",                            # Malformed / completely empty row block
    "usr_203  ; premium ; -15.00 ; billing_error", # Invalid negative numeric revenue anomaly
    "usr_204  ; standard; 19.99  ; active",
    "usr_205  ; premium ; 120.00 ; cancelled"
]

# ==========================================
# 1. Parsing and Gatekeeper Filtration
# ==========================================
print("--- 1. Extraction, Parsing, and Filtration Phase ---")

# Extract header string row to track structure fields
header_fields = [field.strip().lower() for field in RAW_LOGDATA_STREAM[0].split(";")]
print(f"Parsed Ingestion Headers: {header_fields}")

# Process rows: Split by semi-colon delimiter, strip spacing, and filter out null empty rows
# This uses a tail filter to ensure we discard rows where the primary ID field is missing
parsed_rows_matrix = [
    [cell.strip() for cell in row.split(";")]
    for row in RAW_LOGDATA_STREAM[1:] # Exclude the header row from mapping
    if row.strip() and not row.split(";")[0].isspace()
]

print(f"Valid Structured Rows Retained: {len(parsed_rows_matrix)}")


# ==========================================
# 2. Record Transformation & Cleaning
# ==========================================
print("\n--- 2. Data Cleaning and JSON Record Transformation ---")

# Task: Map the flat row arrays into highly readable, typed dictionary structures (JSON equivalent)
# Simultaneously enforce casting constraints: revenue string -> clean float.
# We apply a tail filter to throw out records with anomalous negative revenue streams.
sanitized_user_records = [
    {
        "user_id": row[0].upper(),
        "tier": row[1].upper(),
        "revenue": float(row[2]),
        "status": row[3].lower()
    }
    for row in parsed_rows_matrix
    if float(row[2]) >= 0.0 # Eliminates usr_203 (-15.00) from passing further down the pipe
]

print("Sanitized Master Records Base:")
for record in sanitized_user_records:
    print(f"  {record}")


# ==========================================
# 3. Feature Extraction & Aggregation Prep
# ==========================================
print("\n--- 3. Feature Extraction and Analytical Aggregation ---")

# Task: Isolate numerical revenue values from active premium users to run high-speed calculations
premium_revenue_stream = [
    record["revenue"]
    for record in sanitized_user_records
    if record["tier"] == "PREMIUM" and record["status"] == "active"
]

print(f"Isolated Revenue Array: {premium_revenue_stream}")
# Compute direct aggregate scalar values instantly
total_recurring_yield = sum(premium_revenue_stream)
print(f"Calculated Total Premium ARR Metric: ${total_recurring_yield:.2f}")


# ==========================================
# 4. Preparing Database Inserts
# ==========================================
print("\n--- 4. Final Database Payload Preparation ---")

# Task: Convert our list of dict records into an array of completely immutable tuples
# formatted precisely to pass straight into a raw SQL driver execute batch insert statement.
db_insert_payload = [
    (rec["user_id"], rec["tier"], rec["revenue"], rec["status"])
    for rec in sanitized_user_records
]

print("Generated Batched SQL Target Tuple Array:")
for batch_row in db_insert_payload:
    print(f"  INSERT INTO user_ledger VALUES {batch_row};")

