# ==========================================
# 1. Implicit vs. Explicit Conversion
# ==========================================
print("--- Conversion Paths ---")
# Implicit Coercion: Python converts integer 5 to 5.0 automatically
result_implicit = 5 + 2.5
print(f"Implicit Result: {result_implicit} | Type: {type(result_implicit)}")

# Explicit Casting: Manually changing a string to an integer
age_str = "25"
age_int = int(age_str)
print(f"Explicit Result: {age_int} | Type: {type(age_int)}")


# ==========================================
# 2. Boolean Truthiness (Falsy vs Truthy)
# ==========================================
print("\n--- Truthiness Evaluation ---")
# Testing empty/zero containers vs filled containers
print(f"bool(0):        {bool(0)}")
print(f"bool(''):       {bool('')}")
print(f"bool([]):       {bool([])}")
print(f"bool('False'):  {bool('False')}")  # Filled string! Evaluates to True.


# ==========================================
# 3. Inter-Collection Transformations
# ==========================================
print("\n--- Collection Conversions ---")
source_list = ["apple", "banana", "apple", "cherry"]

# List -> Set (Drops duplicates)
unique_set = set(source_list)
print(f"Unique Set: {unique_set}")

# Set -> Tuple
ordered_tuple = tuple(unique_set)
print(f"Tuple:      {ordered_tuple}")

# Constructing a Dictionary from matching pairs
pairs_list = [("id", 101), ("role", "admin")]
user_dict = dict(pairs_list)
print(f"Generated Dictionary: {user_dict}")


# ==========================================
# 4. Handling Conversion Failures
# ==========================================
print("\n--- Type Conversion Failures ---")

# Scenario A: Structurally impossible data content (ValueError)
try:
    bad_parse = int("123abc45")
except ValueError as err:
    print(f"Caught ValueError: {err}")

# Scenario B: Un-iterable input passed to structural constructor (TypeError)
try:
    bad_structure = list(42)
except TypeError as err:
    print(f"Caught TypeError:  {err}")