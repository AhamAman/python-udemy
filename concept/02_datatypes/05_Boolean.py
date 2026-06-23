# ==========================================
# 1. Comparison & Hidden Integer Nature
# ==========================================
print("--- Boolean Fundamentals ---")
is_valid = True
print(f"Type of True: {type(is_valid)}")

# Proving Booleans are secretly integers under the hood
print(f"True + True = {True + True}")       # Outputs: 2
print(f"False * 100 = {False * 100}")     # Outputs: 0
print(f"Is True equal to 1? {True == 1}") # Outputs: True

# ==========================================
# 2. Logical Operators & Truth Tables
# ==========================================
print("\n--- Logical Operators ---")
has_driver_license = True
has_car = False

# AND requires both conditions to be met
can_drive = has_driver_license and has_car
# OR requires at least one condition to be met
can_take_bus = has_driver_license or has_car

print(f"Can drive? {can_drive}")
print(f"Can take bus? {can_take_bus}")

# ==========================================
# 3. Short-Circuit Evaluation Demo
# ==========================================
print("\n--- Short-Circuit Evaluation ---")

def risky_action():
    print("-> Risky action executed!")
    return True

print("Executing OR (Left side is True):")
# Because the first term is True, Python short-circuits.
# 'risky_action()' is NEVER called, so its print statement won't run.
result_or = True or risky_action()

print("\nExecuting AND (Left side is False):")
# Because the first term is False, an 'and' expression cannot be True.
# Python short-circuits. 'risky_action()' is skipped again.
result_and = False and risky_action()

# Example of using short circuiting to prevent a ZeroDivisionError
denominator = 0
# If denominator == 0 is True, the 'or' stops and never runs the division block!
safe_check = (denominator == 0) or (10 / denominator > 2)
print(f"\nSafe check completed without crashing: {safe_check}")