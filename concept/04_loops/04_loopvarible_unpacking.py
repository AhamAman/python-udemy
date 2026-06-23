# =====================================================================
# 1. SCOPE AND PERSISTENCE
# =====================================================================
print("--- 1. Loop Variable Persistence & Reuse ---")

# Let's define a variable before the loop
number = 999

for number in [1, 2, 3]:
    # The loop overwrites the external 'number' variable
    pass

# Even though the loop is over, 'number' still exists and holds the last value!
print(f"Value of 'number' after the loop: {number}") 

# Throwaway naming convention (_)
for _ in range(2):
    print("Action repeated without using the variable name.")


# =====================================================================
# 2. TUPLE UNPACKING (MULTIPLE LOOP VARIABLES)
# =====================================================================
print("\n--- 2. Tuple Unpacking ---")

# A list containing coordinates (tuples)
coordinates = [(10, 20), (30, 40), (50, 60)]

# We unpack the two elements of each tuple directly into 'x' and 'y'
for x, y in coordinates:
    print(f"X coordinate: {x}, Y coordinate: {y}")


# =====================================================================
# 3. DICTIONARY UNPACKING
# =====================================================================
print("\n--- 3. Dictionary Unpacking ---")

user_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}

# .items() returns a stream of (key, value) tuples, which we unpack
for name, score in user_scores.items():
    print(f"User: {name} | Score: {score}")