# =====================================================================
# DEMO PROGRAM: LOOPING OVER COLLECTIONS IN PYTHON
# =====================================================================

print("--- 1. Looping through Lists ---")
# Lists are ordered and mutable.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")


print("\n--- 2. Looping through Tuples ---")
# Tuples are ordered and immutable (cannot be changed).
coordinates = (10, 20, 30)
for coordinate in coordinates:
    print(f"Coordinate: {coordinate}")


print("\n--- 3. Looping through Strings ---")
# Strings are iterable sequences of characters.
word = "Python"
for letter in word:
    print(f"Letter: {letter}")


print("\n--- 4. Looping through Sets ---")
# Sets are unordered collections of unique elements. 
# Notice how the output order might not match the definition order.
unique_ids = {101, 102, 103, 101} # 101 is duplicated but will only print once
for user_id in unique_ids:
    print(f"User ID: {user_id}")


# Define a dictionary for the next few examples
user_profile = {
    "username": "coder_dan",
    "role": "developer",
    "status": "active"
}

print("\n--- 5. Looping through Dictionaries (Default) ---")
# By default, looping over a dictionary iterates over its keys.
for key in user_profile:
    print(f"Default loop key: {key}")


print("\n--- 6. Looping through Dictionary Keys explicitly ---")
# Using the .keys() method (more explicit than the default loop).
for key in user_profile.keys():
    print(f"Explicit Key: {key}")


print("\n--- 7. Looping through Dictionary Values ---")
# Using the .values() method to access the data without the keys.
for value in user_profile.values():
    print(f"Value: {value}")


print("\n--- 8. Looping through Dictionary Items ---")
# Using the .items() method yields a (key, value) tuple.
# We "unpack" them directly into two separate variables.
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")


print("\n--- 9. Looping through Nested Collections ---")
# A list containing dictionaries, where one key maps to another list.
company_structure = [
    {
        "department": "Engineering",
        "team_leads": ["Alice", "Bob"]
    },
    {
        "department": "Design",
        "team_leads": ["Charlie"]
    }
]

# External Loop: Iterates through the main list (dictionaries)
for dept_info in company_structure:
    print(f"\nDepartment: {dept_info['department']}")
    
    print("Team Leads:")
    # Internal Nested Loop: Iterates through the list inside the dictionary
    for lead in dept_info["team_leads"]:
        print(f" - {lead}")

print("\n=====================================================================")
print("Demo complete!")