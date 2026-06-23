# ==========================================
# 1. Duplicates & Hashability Requirements
# ==========================================
print("--- Set Foundations ---")
# Duplicates are automatically discarded
numbers_set = {1, 2, 2, 3, 3, 3, 4}
print(f"Unique numbers: {numbers_set}")  # Outputs: {1, 2, 3, 4}

# Proving hashability rule
try:
    invalid_set = {1, 2, [3, 4]}  # Fails because a list is mutable/unhashable
except TypeError as error:
    print(f"Caught expected error: {error}")


# ==========================================
# 2. Membership Testing Speed (Concept)
# ==========================================
print("\n--- Membership Testing ---")
ingredients = {"tomato", "onion", "garlic"}
# Instant O(1) evaluation
print(f"Is garlic in the recipe? {'garlic' in ingredients}")


# ==========================================
# 3. Set Operations (Venn Diagram Algebra)
# ==========================================
print("\n--- Set Algebra ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Everything combined
print(f"Union (|):               {set_a | set_b}")

# Intersection: Shared items
print(f"Intersection (&):        {set_a & set_b}")

# Difference: Elements in A but not B
print(f"Difference (-):          {set_a - set_b}")

# Symmetric Difference: In A or B, but not both
print(f"Symmetric Difference (^): {set_a ^ set_b}")


# ==========================================
# 4. Frozen Sets
# ==========================================
print("\n--- Frozen Sets ---")
normal_set = {1, 2}
frozen = frozenset([3, 4, 5])

print(f"Frozen set type: {type(frozen)}")

try:
    frozen.add(6)  # This will fail
except AttributeError as error:
    print(f"Caught expected error: {error}")

# Because a frozenset is hashable, it can be nested inside a normal set!
nested_set = {normal_set, frozen} # Throws error if you try it with two normal sets
print(f"Set containing a frozenset: {nested_set}")