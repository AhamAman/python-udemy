# ==========================================
# 1. Deterministic Nature of Hashing
# ==========================================
print("--- Hashing Fundamentals ---")
text_a = "Python Data Architecture"
text_b = "Python Data Architecture"

print(f"Hash of text_a: {hash(text_a)}")
print(f"Hash of text_b: {hash(text_b)}")
print(f"Are hashes identical? {hash(text_a) == hash(text_b)}")


# ==========================================
# 2. Hashable vs. Unhashable Verification
# ==========================================
print("\n--- Hashability Boundaries ---")

# An immutable tuple is perfectly hashable
valid_tuple = (1, 2, 3)
print(f"Tuple Hash: {hash(valid_tuple)}")

# Attempting to hash a mutable list fails
invalid_list = [1, 2, 3]
try:
    hash(invalid_list)
except TypeError as error:
    print(f"Caught expected error: {error}")


# ==========================================
# 3. Collection Constraints in Action
# ==========================================
print("\n--- Collection Requirements ---")

# Valid: Using a tuple as a dictionary key
coordinates_dict = {(40.7, -74.0): "New York"}
print(f"Dictionary lookup via tuple key: {coordinates_dict[(40.7, -74.0)]}")

# Invalid: Trying to use a list as a dictionary key or set item
try:
    bad_dict = {[1, 2]: "Invalid Key"}
except TypeError as error:
    print(f"Dictionary constraint block: {error}")


# ==========================================
# 4. Hash Interning Safety (Security Note)
# ==========================================
print("\n--- Python Security: Hash Seed Randomization ---")
# If you run this file multiple times, you will notice that the hashes for strings 
# change every time you restart the script. 
# This is a built-in security feature called "Hash Randomization" designed to prevent 
# Denial of Service (DoS) attacks where hackers deliberately try to trigger 
# mass hash collisions to slow down web servers.
print(f"String runtime unique hash: {hash('secure_string')}")