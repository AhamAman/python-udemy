# ==========================================
# 1. STRUCTURING CUSTOM DOMAIN EXCEPTIONS
# ==========================================

class InsufficientFundsError(Exception):
    """Custom exception raised when an account violates credit limits."""
    pass


# ==========================================
# 2. THE INFRASTRUCTURE LAYER (Raises Exceptions)
# ==========================================

class BankAccountNode:
    def __init__(self, account_id: str, initial_balance: float):
        self.account_id = account_id
        self.balance = float(initial_balance)

    def process_withdrawal(self, amount: float):
        """Applies validation rules and enforces hard business constraints."""
        
        # Guardrail 1: Input Validation (Using a built-in exception)
        if amount <= 0:
            raise ValueError(f"Transaction Rejected: Withdrawal request must be positive. Attempted: {amount}")

        # Guardrail 2: Business Rule Enforcement (Using a domain custom exception)
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Transaction Rejected: Insufficient balance for account '{self.account_id}'. "
                f"Available: ${self.balance:.2f} | Requested: ${amount:.2f}"
            )

        # State modification only occurs if all guardrails clear safely
        self.balance -= amount
        print(f"   [Account Node] Debited ${amount:.2f}. New Balance: ${self.balance:.2f}")


# ==========================================
# 3. THE MIDDLEWARE INTERCEPTOR LAYER (Re-Raises Exceptions)
# ==========================================

def global_transaction_broker(account_node: BankAccountNode, debit_amount: float):
    print(f"\n>>> Broker processing request for Node: '{account_node.account_id}'...")
    
    try:
        # Relaying action down to the core node
        account_node.process_withdrawal(debit_amount)
        
    except InsufficientFundsError as business_error:
        # PARTIAL HANDLING PATTERN:
        # We intercept the error at this middleware layer because we want to perform 
        # an isolated, infrastructure-specific task (telemetry logging) right away.
        print(f"   [Broker Log] ⚠️ AUDIT ALERT: High-risk transaction blocked on {account_node.account_id}.")
        print(f"   [Broker Log] Diagnostic Detail: {business_error}")
        
        # RE-RAISING THE EXCEPTION:
        # Using the 'raise' keyword on a line by itself tells Python to pass the 
        # original exception object up to the next outer layer *without* altering the stack trace.
        raise


# ==========================================
# 4. THE CUSTOMER FRONTEND ENDPOINT (Final Catch)
# ==========================================
print("--- Scenario A: Safe Validation Clear ---")
vault_node = BankAccountNode(account_id="ACC-9941", initial_balance=500.00)
global_transaction_broker(vault_node, 150.00)


print("\n--- Scenario B: Tripping Fail-Fast Input Guardrails ---")
try:
    global_transaction_broker(vault_node, -50.00)
except ValueError as error:
    print(f"[Frontend UI View] Client Formatting Error: {error}")


print("\n--- Scenario C: The Re-Raising Lifecycle Matrix ---")
try:
    # This will trigger an InsufficientFundsError inside BankAccountNode,
    # pass through the global_transaction_broker log hook, and bubble up here.
    global_transaction_broker(vault_node, 9000.00)
    
except InsufficientFundsError:
    # The frontend catches the re-raised exception to present a clean notification to the user
    print("[Frontend UI View] 📱 Displaying message: 'Declined. Please check your credit resources.'")