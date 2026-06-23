class AutomatedVault:
    def __init__(self, owner: str, initial_balance: float, pin: str):
        # Setting up internal object state
        self.owner = owner
        self._balance = initial_balance
        self._pin = pin
        self.system_logs = []

    # ==========================================
    # 1. CORE INSTANCE METHOD & RETURN VALUES
    # ==========================================
    def get_balance(self, entered_pin: str) -> float:
        """
        An instance method that verifies access and returns a value.
        'self' is implicitly passed by Python at runtime.
        """
        # Method calling another internal method to centralize validation logic
        if not self._verify_pin(entered_pin):
            self._log_event("Unauthorized balance check attempt.")
            return -1.0  # Sentinel error return value
            
        self._log_event("Balance successfully viewed.")
        return self._balance

    # ==========================================
    # 2. METHODS CALLING METHODS (Internal Processing)
    # ==========================================
    def deposit_funds(self, amount: float, entered_pin: str) -> bool:
        """Executes a state change after passing internal method validations."""
        if amount <= 0:
            print("   [Vault Error] Deposit amount must be positive.")
            return False

        if not self._verify_pin(entered_pin):
            self._log_event(f"Failed deposit attempt of ${amount}.")
            return False

        # Modifying state safely inside the object boundaries
        self._balance += amount
        self._log_event(f"Deposited ${amount}.")
        return True

    # ==========================================
    # 3. INTERNAL METHOD ORGANIZATION (Private Helpers)
    # ==========================================
    # Methods prefixed with a single underscore are a convention telling 
    # other developers: "This is an internal utility method. Do not call it from outside."
    
    def _verify_pin(self, entered_pin: str) -> bool:
        """Internal helper method used to encapsulate validation rules."""
        return entered_pin == self._pin

    def _log_event(self, description: str):
        """Internal helper method used to maintain audit trails."""
        self.system_logs.append(description)
        print(f"   [System Log Internal] Log recorded: {description}")


# ==========================================
# RUNNING THE METHOD PIPELINE
# ==========================================
print("--- Phase 1: Object Instantiation ---")
vault = AutomatedVault(owner="Alice", initial_balance=5000.0, pin="4321")


print("\n--- Phase 2: Method Invocation & Binding Mechanics ---")

# 1. Calling a method with a failing condition
# Notice we pass 1 argument ('entered_pin'), but the definition has 2 parameters (self, entered_pin)
# Python binds 'vault' directly to 'self' automatically.
print("Attempting balance query with bad PIN...")
bad_query = vault.get_balance(entered_pin="9999")
print(f"Returned Balance Payload: {bad_query}")


# 2. Calling a method with a passing condition (Methods cascading calls internally)
print("\nAttempting structural deposit...")
success_flag = vault.deposit_funds(amount=1500.0, entered_pin="4321")
print(f"Transaction Success Status: {success_flag}")


print("\n--- Phase 3: Explicit Method Binding Introspection ---")

# To prove that 'vault.get_balance("4321")' is just syntactic sugar for passing the object manually,
# we can call the method directly from the Class namespace and pass the instance explicitly:
explicit_call_val = AutomatedVault.get_balance(vault, entered_pin="4321")
print(f"Explicit Class-Level Call Result: ${explicit_call_val}")