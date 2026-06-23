# ==========================================
# 1. Division, Floor Division, and Modulus
# ==========================================
print("--- Division Behaviors ---")
print(f"True Division (7 / 2):  {7 / 2}  (Type: {type(7 / 2)})")
print(f"Floor Division (7 // 2): {7 // 2}  (Type: {type(7 // 2)})")
print(f"Modulus Remainder (7 % 2): {7 % 2}")

# The negative floor division catch
print(f"Negative Floor Division (-7 // 2): {-7 // 2} (Rounds down towards -infinity)")

# ==========================================
# 2. Arbitrary Precision (No Overflow)
# ==========================================
print("\n--- Python's Massive Integers ---")
# A standard 64-bit integer maxes out around 9 x 10^18
large_int = 2 ** 200  # 2 raised to the 200th power
print(f"2^200 = {large_int}")
print(f"Type is still just: {type(large_int)}")

# ==========================================
# 3. Floating-Point Precision Trap
# ==========================================
print("\n--- The Floating-Point Trap ---")
# Classic computer science quirk due to binary representation limits
sum_float = 0.1 + 0.2
print(f"Is 0.1 + 0.2 exactly 0.3? {sum_float == 0.3}")
print(f"Actual value of 0.1 + 0.2: {sum_float:.17f}")

# How to fix it if you need exact math (e.g., money)
from decimal import Decimal
exact_sum = Decimal('0.1') + Decimal('0.2')
print(f"Fixed using Decimal class: {exact_sum} (Type: {type(exact_sum)})")