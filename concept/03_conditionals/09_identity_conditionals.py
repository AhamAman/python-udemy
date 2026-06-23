# ==========================================
# 1. Structural Equality vs. Absolute Identity
# ==========================================
print("--- Equality vs Identity Mechanics ---")
# Instantiate two lists with identical elements
list_1 = [10, 20, 30]
list_2 = [10, 20, 30]

print(f"Value check (list_1 == list_2): {list_1 == list_2}") # True (contents match)
print(f"ID check    (list_1 is list_2): {list_1 is list_2}") # False (stored in different memory locations)

print(f"  Memory Address 1: {id(list_1)}")
print(f"  Memory Address 2: {id(list_2)}")


# ==========================================
# 2. Aliasing (Shared Identity)
# ==========================================
print("\n--- Aliasing / Shared Reference ---")
# Point list_3 to the exact same pointer as list_1
list_3 = list_1

print(f"Is list_3 the same object as list_1? {list_3 is list_1}") # True
# A change to list_3 modifies the shared block in RAM
list_3.append(999)
print(f"Original list_1 after alias modification: {list_1}")


# ==========================================
# 3. Why 'is None' Shields Against Exploits
# ==========================================
print("\n--- The 'is None' Safety Shield ---")

class MaliciousMock:
    def __eq__(self, other):
        # This custom method intercepts '==' and lies, claiming it matches everything!
        return True

fake_data = MaliciousMock()

# Value equality is fooled by the overwritten method
print(f"Testing spoofed object with '== None': {fake_data == None}") # Returns True (Exploited!)

# Identity verification looks at raw memory addresses and protects the code path
print(f"Testing spoofed object with 'is None': {fake_data is None}") # Returns False (Protected!)