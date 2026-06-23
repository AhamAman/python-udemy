# ==========================================
# 1. Standard Truthy vs. Falsy Verification
# ==========================================
print("--- Standard Truthiness Evaluations ---")

def check_truthiness(name, element):
    # Forcing the element into a boolean context
    print(f"Value: {str(element):12} | bool() resolves to: {bool(element)}")

check_truthiness("Integer Zero", 0)
check_truthiness("Integer Non-Zero", 42)
check_truthiness("Empty String", "")
check_truthiness("Filled String", "Hello")
check_truthiness("Empty List", [])


# ==========================================
# 2. Idiomatic (Pythonic) Conditional Code
# ==========================================
print("\n--- Idiomatic Python Usage ---")
# Simulating database query results
retrieved_users = ["alice", "bob"]

# UN-PYTHONIC WAY: Explicitly checking the length layout
if len(retrieved_users) > 0:
    print("Un-pythonic check: Users found!")

# PYTHONIC WAY: Leveraging implicit truthiness
if retrieved_users:
    print("Pythonic check:    Users found!")


# ==========================================
# 3. Custom Truthiness Implementation
# ==========================================
print("\n--- Custom Object Truthiness ---")

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Overriding the internal boolean resolution rules
    def __bool__(self):
        # An account evaluates to False if it has zero or negative funds
        return self.balance > 0

# Scenario A: Account with funds
premium_acct = Account("Sarah", 500.00)
# Scenario B: Overdrawn account
broke_acct = Account("Alex", -50.00)

print(f"Sarah's Account Truthiness: {bool(premium_acct)}")
print(f"Alex's Account Truthiness:  {bool(broke_acct)}")

# Using the custom objects directly inside control flow branches
if not broke_acct:
    print("Alert: Frozen status triggered due to insufficient account logic!")