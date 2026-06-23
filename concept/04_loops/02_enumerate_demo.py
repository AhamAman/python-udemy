# =====================================================================
# DEMO: USING ENUMERATE() IN PYTHON LOOPS
# =====================================================================

tasks = ["Write code", "Run tests", "Deploy app", "Celebrate"]

print("--- 1. The Old/Clunky Way (range + len) ---")
# This requires looking up the item by index manually on every iteration.
for i in range(len(tasks)):
    print(f"Task {i}: {tasks[i]}")


print("\n--- 2. The Pythonic Way (enumerate) ---")
# enumerate() tracks the index and item cleanly in one shot.
for index, task in enumerate(tasks):
    print(f"Index {index} -> Task: {task}")


print("\n--- 3. Changing the Starting Index (The 'start' Argument) ---")
# Humans usually don't count from 0. 
# You can pass a 'start' argument to make your logs or UI friendlier.
for position, task in enumerate(tasks, start=1):
    print(f"Step {position}: {task}")


print("\n--- 4. What Enumerate actually generates under the hood ---")
# If you don't unpack it, enumerate yields an 'enumerate object' 
# that produces tuples when evaluated.
enum_object = enumerate(tasks)
print(f"Object type: {type(enum_object)}")

# Let's peek at the actual data stream by forcing it into a list:
print(f"As a raw list of tuples: {list(enum_object)}")


print("\n=====================================================================")
print("Demo complete!")