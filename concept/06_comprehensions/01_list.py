# ==========================================
# 1. Translating a Loop into a Comprehension
# ==========================================
print("--- 1. Structural Comparison ---")

raw_voltages = [12, 24, 48, 110]

# Paradigm A: Imperative For-Loop
voltages_loop = []
for v in raw_voltages:
    voltages_loop.append(v * 2)
print(f"Loop Output:          {voltages_loop}")

# Paradigm B: Declarative List Comprehension
# [Expression  |  Iteration Context]
voltages_comp = [v * 2 for v in raw_voltages]
print(f"Comprehension Output: {voltages_comp}")


# ==========================================
# 2. String Transformations and Conversions
# ==========================================
print("\n--- 2. Building Structural Transformations ---")

cluster_nodes = ["  node-alpha  ", "node-beta ", " node-gamma"]

# Clean and normalize strings inline
sanitized_nodes = [node.strip().upper() for node in cluster_nodes]
print(f"Sanitized Data Records: {sanitized_nodes}")


# ==========================================
# 3. Common Beginner Mistakes & Traps
# ==========================================
print("\n--- 3. Traps and Anti-Patterns ---")

# Mistake 1: The Forgotten Return Trap
# Trying to execute an in-place mutation method that returns None
buggy_names = ["alice", "bob", "charlie"]
# .upper() returns a new string, but .append() or structural list mutations inside return None!
broken_comprehension = [name.upper() for name in buggy_names] # Correct pattern
print(f"Correct Transform: {broken_comprehension}")

# Mistake 2: Appending Inside the Comprehension (Double Append Bug)
# A comprehension automatically drops the expression value into the new list.
# Writing .append() INSIDE the expression creates an array of 'None' objects!
double_append_trap = [voltages_loop.append(x) for x in [1, 2, 3]]
print(f"Double Append Result (Incorrect!): {double_append_trap}")