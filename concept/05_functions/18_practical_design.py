import math

# Simulated global state database
GLOBAL_USER_DB = {"USR_101": {"tier": "free", "balance": 45.00}}

# ==========================================
# 1. The Monolithic Anti-Pattern (What NOT to do)
# ==========================================
# Problems: Low Cohesion, Highly Coupled to Global State, Multiple Responsibilities, Side-Effects
def process_everything_trap(user_id, item_cost):
    # Responsibility 1: Fetching data from global scopes (Coupled)
    user = GLOBAL_USER_DB.get(user_id)
    if user is None:
        print("[LOG] User missing") # Side effect: IO printing
        return False
        
    # Responsibility 2: Calculating dynamic business rule pricing
    final_price = item_cost
    if user["tier"] == "premium":
        final_price = item_cost * 0.90
    elif user["tier"] == "free":
        final_price = item_cost + 5.00 # Delivery fee
        
    # Responsibility 3: Mutating state external to itself
    if user["balance"] >= final_price:
        user["balance"] -= final_price
        print(f"[LOG] Debited user. Remaining: {user['balance']}")
        return True
    else:
        return False


# ==========================================
# 2. Clean, Refactored Production Architecture
# ==========================================

# Primitive A: Pure Function (Deterministic, Zero Side Effects, High Cohesion)
def calculate_adjusted_price(base_cost: float, user_tier: str) -> float:
    """Computes exact price matching tier rules. Completely pure."""
    if user_tier == "premium":
        return base_cost * 0.90
    if user_tier == "free":
        return base_cost + 5.00
    return base_cost

# Primitive B: Pure Function (Deterministic Safety Gate)
def can_afford_purchase(balance: float, cost: float) -> bool:
    """Evaluates financial boundary clearance."""
    return balance >= cost

# Primitive C: Stateful Side-Effect Handler (Explicitly manages boundary mutations)
def apply_wallet_debit(user_record: dict, amount: float) -> None:
    """Mutates specific dictionary records in place. Side-effect explicit."""
    user_record["balance"] -= amount


# Orchestration Layer (The Pipeline Controller)
def execute_order_pipeline(user_id: str, item_cost: float, database: dict) -> bool:
    """Coordinates independent clean primitives to fulfill a transaction process."""
    user = database.get(user_id)
    if user is None:
        return False
        
    # Linear calculation flow utilizing isolated building blocks
    target_price = calculate_adjusted_price(item_cost, user["tier"])
    
    if not can_afford_purchase(user["balance"], target_price):
        return False
        
    apply_wallet_debit(user, target_price)
    return True


# ==========================================
# Execution Run
# ==========================================
print("--- Running Clean Refactored Pipeline ---")
success = execute_order_pipeline("USR_101", item_cost=20.00, database=GLOBAL_USER_DB)
print(f"Transaction Status: {success}")
print(f"Updated Clean Database State: {GLOBAL_USER_DB['USR_101']}")