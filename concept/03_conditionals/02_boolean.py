# ==========================================
# 1. Internal Integer Representation
# ==========================================
print("--- Internal Representation ---")
print(f"Type of True: {type(True)}")

# Proving Booleans are subclasses of integers
print(f"Is True an instance of int? {isinstance(True, int)}") 
print(f"Mathematical Value (True + True + False): {True + True + False}") # 1 + 1 + 0 = 2


# ==========================================
# 2. Operators Generating Booleans
# ==========================================
print("\n--- Boolean Generation ---")
x = [1, 2, 3]
y = [1, 2, 3]

# Comparison vs Identity
print(f"Value Equality (x == y): {x == y}")  # Evaluates to True
print(f"Identity Match (x is y): {x is y}")  # Evaluates to False (separate lists in RAM)


# ==========================================
# 3. How Python Forces Expressions to Booleans
# ==========================================
print("\n--- Conditional Expression Collapse ---")
user_list = ["admin_user"]

# The expression 'user_list' is a list object, not a boolean.
# Python implicitly runs bool(user_list) behind the scenes.
if user_list: 
    print("The conditional collapsed to True because the collection is not empty.")

# Re-assigning to a falsy value
user_list = []
if not user_list:
    print("The conditional collapsed to False because the collection is empty.")
    