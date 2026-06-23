import os
from datetime import datetime

# Simulated Configuration State
ENV_CONFIG = {
    "DB_CONNECTED": True,
    "ACTIVE_FEATURES": {"beta_ui": True, "crypto_checkout": False}
}

# Simulated Database Record
MOCK_USER = {
    "username": "alice_dev",
    "is_authenticated": True,
    "role": "editor", # Roles: guest, editor, admin
}

# ==========================================
# 1. Configuration & Startup Guard Patterns
# ==========================================
def verify_system_readiness():
    print("--- 1. Configuration Checks ---")
    
    # Fail-fast pattern on boot
    if not ENV_CONFIG.get("DB_CONNECTED"):
        raise SystemError("CRITICAL: Database connection missing. Boot halted.")
        
    print("System infrastructure integrity: VERIFIED\n")


# ==========================================
# 2. Input, Form, and Business Rule Guards
# ==========================================
def register_new_account(username, password, age):
    print("--- 2. Input & Business Rule Validation ---")
    
    # Guard 1: Input Type & Presence Check
    if not username or not password:
        return {"status": 400, "msg": "Invalid payload: Fields cannot be empty."}
        
    # Guard 2: Form Format Rule
    if len(password) < 8:
        return {"status": 400, "msg": "Security constraint: Password must be >= 8 chars."}
        
    # Guard 3: Complex Business Rule Validation
    if age < 13:
        return {"status": 403, "msg": "Compliance error: User fails COPPA legal age limit."}
        
    # Happy Path (Kept flat and un-nested)
    return {"status": 201, "msg": f"Account '{username}' initialized successfully."}


# ==========================================
# 3. Access Control & Feature Flag Checks
# ==========================================
def delete_article_endpoint(user, feature_name):
    print("--- 3. Access Control & Feature Flags ---")
    
    # Guard 1: User Authentication Validation
    if not user.get("is_authenticated"):
        return {"status": 401, "msg": "Unauthenticated: Missing valid token."}
        
    # Guard 2: Access Control Layer (RBAC)
    if user.get("role") not in ["editor", "admin"]:
        return {"status": 403, "msg": "Unauthorized: Insufficient permissions."}
        
    # Guard 3: Operational Feature Flag Check
    if not ENV_CONFIG["ACTIVE_FEATURES"].get(feature_name, False):
        return {"status": 503, "msg": f"Feature flag '{feature_name}' is currently disabled."}
        
    return {"status": 200, "msg": "Resource successfully deleted."}


# ==========================================
# 4. Data Filtering & API Response Guards
# ==========================================
def process_external_api_payload(raw_json_response):
    print("--- 4. Data Filtering & API Validation ---")
    
    # Schema Structural Integrity Check
    if "data" not in raw_json_response or "status_code" not in raw_json_response:
        return {"error": "API Corruption: Response failed schema structural expectations."}
        
    # Short-circuit checking if status is healthy before extraction
    if raw_json_response["status_code"] != 200:
        return {"error": f"Upstream service failure code: {raw_json_response['status_code']}"}
        
    # Data Filtering Pattern
    raw_metrics = raw_json_response["data"]
    filtered_metrics = [m for m in raw_metrics if m.get("value", 0) > 100]
    
    return {"success": True, "processed_records": filtered_metrics}


# ==========================================
# Execution Run
# ==========================================
verify_system_readiness()

# Test Input/Business validation
reg_attempt = register_new_account("bob_builder", "pass123", age=11)
print(f"Registration Result: {reg_attempt}\n")

# Test Access Control and disabled Feature Flag
api_attempt = delete_article_endpoint(MOCK_USER, feature_name="crypto_checkout")
print(f"API Mutation Result: {api_attempt}\n")

# Test API Response validation
mock_payload = {"status_code": 200, "data": [{"id": 1, "value": 50}, {"id": 2, "value": 250}]}
filter_attempt = process_external_api_payload(mock_payload)
print(f"Filtered Results:    {filter_attempt}")

