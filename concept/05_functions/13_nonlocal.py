# ==========================================
# 1. State Modification in Action
# ==========================================
def initialize_ledger(starting_balance):
    """Outer function defining our enclosing core variable tier."""
    balance = starting_balance  # Enclosing Variable (E)
    
    def apply_transaction(amount, transaction_type):
        # We must explicitly step outside our local bubble to mutate 'balance'
        nonlocal balance
        
        if transaction_type == "CREDIT":
            balance += amount
        elif transaction_type == "DEBIT":
            if amount > balance:
                return f"[REJECTED] Insufficient funds. Available: ${balance}"
            balance -= amount
            
        return f"[SUCCESS] Updated Ledger Balance: ${balance}"
        
    return apply_transaction


# Instantiate a persistent ledger closure instance
my_wallet = initialize_ledger(starting_balance=100)

print("--- 1. Valid Nonlocal State Mutations ---")
print(my_wallet(50, "CREDIT"))  # 100 + 50 = 150
print(my_wallet(30, "DEBIT"))   # 150 - 30 = 120
print(my_wallet(200, "DEBIT"))  # Rejected!


# ==========================================
# 2. Compilation Protection Rules
# ==========================================
print("\n--- 2. Compiler Enforcement Constraints ---")

# Demonstrating why nonlocal requires pre-existing variables:
try:
    exec("""
def outer_scope_test():
    def inner_scope_test():
        nonlocal untracked_variable # Fails instantly because it doesn't exist one layer up
        untracked_variable = 50
    inner_scope_test()
    """)
except SyntaxError as err:
    print(f"Caught expected SyntaxError: {err}")

