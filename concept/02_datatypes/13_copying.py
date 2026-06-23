import copy
import sys

# ==========================================
# 1. Assignment vs. Copying (Shared Reference)
# ==========================================
print("--- Assignment vs. Copying ---")
original_list = [1, 2, 3]
assigned_list = original_list  # Creates an alias (shared reference)

print(f"Are original and assigned the same object? {original_list is assigned_list}")
print(f"Memory ID Original: {id(original_list)}")
print(f"Memory ID Assigned: {id(assigned_list)}")

# Mutating the assignment ruins the original
assigned_list.append(99)
print(f"Original after assignment mutation: {original_list}")


# ==========================================
# 2. The Shallow Copy Trap
# ==========================================
print("\n--- The Shallow Copy Trap ---")
# Nested list structure: a matrix row inside an outer list
nested_source = [[1, 2], [3, 4]]
shallow_version = copy.copy(nested_source)

print(f"Outer layer identity match? {nested_source is shallow_version}") # False (Containers are unique)
print(f"Inner layer identity match? {nested_source[0] is shallow_version[0]}") # True! (Pointers are shared)

# Mutation Side-Effect:
# Modifying the outer container is safe...
shallow_version.append([5, 6])
# But modifying a shared nested object bleeds backwards into the source!
shallow_version[0][0] = 999

print(f"Shallow Copy:    {shallow_version}")
print(f"Original Source: {nested_source}  <- (Nested item corrupted!)")


# ==========================================
# 3. The Deep Copy Resolution
# ==========================================
print("\n--- The Deep Copy Resolution ---")
nested_source_2 = [[1, 2], [3, 4]]
deep_version = copy.deepcopy(nested_source_2)

print(f"Outer layer match? {nested_source_2 is deep_version}")    # False
print(f"Inner layer match? {nested_source_2[0] is deep_version[0]}") # False! (Recursively duplicated)

# Mutating the deep copy nested array has zero side-effects
deep_version[0][0] = 77777

print(f"Deep Copy:        {deep_version}")
print(f"Original Source2: {nested_source_2}  <- (Completely protected!)")