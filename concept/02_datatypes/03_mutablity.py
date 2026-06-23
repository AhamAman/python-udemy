# ==========================================
# 1. Identity vs Value Equality (== vs is)
# ==========================================
print("--- Equality vs Identity ---")
# Create two structurally identical lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print(f"Value comparison (list_a == list_b): {list_a == list_b}")  # True (same data)
print(f"Identity comparison (list_a is list_b): {list_a is list_b}")  # False (different boxes in RAM)

print(f"Memory Address A: {id(list_a)}")
print(f"Memory Address B: {id(list_b)}")


# ==========================================
# 2. Aliasing and Mutable Side Effects
# ==========================================
print("\n--- Aliasing and Mutation Side Effects ---")
# list_c is NOT a copy; it's an alias pointing to the exact same RAM location as list_a
list_c = list_a

print(f"Is list_c an alias of list_a? {list_c is list_a}")  # True

# Modifying list_c updates the shared memory block!
list_c.append(99)

print(f"list_c after mutation: {list_c}")
print(f"list_a after mutation: {list_a}  <- (Boom! It changed here too!)")


# ==========================================
# 3. Immutable Behavior Under Modification
# ==========================================
print("\n--- Immutable Object Behavior ---")
x = 10
initial_id = id(x)
print(f"Initial 'x' value: {x} | Memory ID: {initial_id}")

# Modifying an int looks like it mutates, but it actually spawns a new object
x = x + 1
new_id = id(x)
print(f"Updated 'x' value: {x} | Memory ID: {new_id}")
print(f"Did the memory address change? {initial_id != new_id}")


# ==========================================
# 4. Small Object Interning (Python Optimization Quirky Exception)
# ==========================================
print("\n--- Python Optimization: Integer Caching ---")
# To save memory, Python pre-allocates small integers (-5 to 256) at startup.
num1 = 100
num2 = 100
print(f"Do num1 and num2 share a physical object? {num1 is num2}")  # True!

# Larger numbers bypass this cache and create separate memory allocations
large1 = 999999
large2 = 999999
print(f"Do large1 and large2 share an object?     {large1 is large2}")  # False!