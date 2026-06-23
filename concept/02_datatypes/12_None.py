# ==========================================
# 1. The Singleton & Identity Demonstration
# ==========================================
print("--- The Nature of None ---")
val1 = None
val2 = None

print(f"Type of None: {type(val1)}")
print(f"Are both None references pointing to the same RAM location? {val1 is val2}")
print(f"Memory ID: {id(val1)}")


# ==========================================
# 2. None vs. Empty Containers
# ==========================================
print("\n--- None vs Empty Containers ---")
empty_box = []      # A real list exists in memory, it just has no items
non_existent = None # No list, no data, pure absence

print(f"Is empty_box equivalent to None?     {empty_box == None}") # False
print(f"Are both considered Falsy?           {bool(empty_box) == bool(non_existent)}") # True


# ==========================================
# 3. Explicit vs Implicit Function Returns
# ==========================================
print("\n--- Function Returns ---")

def implicit_return_func():
    print("-> Doing some work...")
    # No return statement explicitly defined

def explicit_return_func(found_data):
    if not found_data:
        return None # Explicitly telling the caller "no data was found"
    return "Data Payload"

result_implicit = implicit_return_func()
result_explicit = explicit_return_func(found_data=False)

# Every Python function returns None automatically if you don't specify a return value
print(f"Implicit return value: {result_implicit}")
print(f"Explicit return value: {result_explicit}")


# ==========================================
# 4. Safe Verification Guardrails
# ==========================================
print("\n--- The Correct Verification Pattern ---")
current_user = None

# Correct Pythonic way to guard against missing data
if current_user is None:
    print("Action blocked: No user session active.")

# Why 'is' is safer than '==': Preventing custom class spoofing
class DeceptiveClass:
    def __eq__(self, other):
        return True # Lies and claims it is equal to everything!

fake_object = DeceptiveClass()

print(f"Testing spoofed object with '== None': {fake_object == None}") # Returns True (Fooled!)
print(f"Testing spoofed object with 'is None': {fake_object is None}") # Returns False (Protected!)