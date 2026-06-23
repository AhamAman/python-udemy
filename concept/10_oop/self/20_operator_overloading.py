class FinancialLedger:
    def __init__(self, currency: str, balance: float):
        self.currency = currency.upper()
        self.balance = float(balance)

    def __repr__(self) -> str:
        return f"FinancialLedger(currency='{self.currency}', balance={self.balance:.2f})"

    # ==========================================
    # 1. ARITHMETIC OPERATOR OVERLOADING
    # ==========================================

    def __add__(self, other) -> 'FinancialLedger':
        """Overloads the addition operator (+) to merge two balance pools."""
        if not isinstance(other, FinancialLedger):
            raise TypeError("Addition operator can only combine two FinancialLedger objects.")
            
        if self.currency != other.currency:
            raise ValueError(f"Currency Mismatch: Cannot directly add {self.currency} and {other.currency} without a spot rate.")
            
        # Returns a brand-new object instance to preserve immutable state histories
        return FinancialLedger(currency=self.currency, balance=self.balance + other.balance)

    def __sub__(self, other) -> 'FinancialLedger':
        """Overloads the subtraction operator (-) to calculate resource deductions."""
        if not isinstance(other, FinancialLedger):
            raise TypeError("Subtraction operator can only run between identical ledger objects.")
            
        if self.currency != other.currency:
            raise ValueError(f"Currency Mismatch: Cannot subtract different currency denominators.")
            
        return FinancialLedger(currency=self.currency, balance=self.balance - other.balance)

    # ==========================================
    # 2. COMPARISON & EQUALITY OVERLOADING
    # ==========================================

    def __eq__(self, other) -> bool:
        """Overloads the equality operator (==) to assess structural value similarity."""
        if not isinstance(other, FinancialLedger):
            return False
        return self.currency == other.currency and self.balance == other.balance

    def __lt__(self, other) -> bool:
        """Overloads the less-than operator (<) to enable sorting operations."""
        if not isinstance(other, FinancialLedger):
            raise TypeError("Comparison requires matching type models.")
            
        if self.currency != other.currency:
            raise ValueError("Cannot compare values across contrasting currency layers.")
            
        return self.balance < other.balance


# ==========================================
# RUNNING THE ALGEBRAIC LEDGER SYSTEM
# ==========================================
print("--- Phase 1: Context Setup ---")
ledger_q1 = FinancialLedger(currency="USD", balance=5000.00)
ledger_q2 = FinancialLedger(currency="USD", balance=2500.50)
ledger_intl = FinancialLedger(currency="EUR", balance=3000.00)

print(f"Ledger A: {ledger_q1}")
print(f"Ledger B: {ledger_q2}")


print("\n--- Phase 2: Evaluating Arithmetic Expressions ---")

# Python catches the '+', routes to ledger_q1.__add__(ledger_q2)
combined_vault = ledger_q1 + ledger_q2
print(f"Result of Algebraic Fusion (A + B): {combined_vault}")

# Python catches the '-', routes to ledger_q1.__sub__(ledger_q2)
net_delta = ledger_q1 - ledger_q2
print(f"Result of Balance Deduction (A - B): {net_delta}")


print("\n--- Phase 3: Evaluating Logical Comparison Trees ---")

# Evaluating overloaded equalities and relational sorters
print(f"Does Ledger A equal Ledger B? (A == B): {ledger_q1 == ledger_q2}")
print(f"Is Ledger B smaller than Ledger A? (B < A): {ledger_q2 < ledger_q1}")

# Rich Benefit: Because __lt__ is implemented, Python can automatically sort collections for us!
ledger_pool = [ledger_q1, ledger_q2]
print(f"Auto-Sorted Ledger Portfolio: {sorted(ledger_pool)}")


print("\n--- Phase 4: Defensive Boundary Crashes ---")
try:
    print("Attempting an illegal multi-currency operation...")
    invalid_merge = ledger_q1 + ledger_intl
except ValueError as e:
    print(f"❌ Operation Intercepted & Blocked Safely: {e}")