# ==========================================
# 1. Standard Comparison Layout
# ==========================================
print("--- Standard vs. Ternary Layout ---")
score = 85

# The traditional 4-line control flow approach
if score >= 50:
    result_traditional = "Pass"
else:
    result_traditional = "Fail"

# The elegant 1-line expression approach
# Note: It evaluates the condition FIRST, then selects the value side
result_ternary = "Pass" if score >= 50 else "Fail"

print(f"Traditional Result: {result_traditional}")
print(f"Ternary Result:     {result_ternary}")


# ==========================================
# 2. Inline Evaluation & Short-Circuit Proof
# ==========================================
print("\n--- Inline Processing Performance ---")
user_role = "guest"

# You can use ternary expressions directly inside other operations, like print()
print(f"Access Privilege Tier: {'HIGH' if user_role == 'admin' else 'LOW'}")


# ==========================================
# 3. The Nested Trap (What NOT to do)
# ==========================================
print("\n--- The Nested Complexity Trap ---")
signal_strength = -75 # dBm

# Un-nested, clean alternative layout
if signal_strength > -60:
    quality = "Excellent"
elif signal_strength > -80:
    quality = "Good"
else:
    quality = "Poor"

# Nested Ternary equivalent (Hard to scan, prone to calculation errors during code reviews)
quality_nested = "Excellent" if signal_strength > -60 else "Good" if signal_strength > -80 else "Poor"

print(f"Evaluated Signal Quality: {quality_nested}")

