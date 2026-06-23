# ==========================================
# 1. Assignment vs. Equality Comparison
# ==========================================
print("--- Assignment vs. Equality ---")
# Active Action: Storing the value 15 inside the variable 'score'
score = 15 

# Passive Question: Checking the value
is_perfect_score = (score == 100)
print(f"Is score equal to 100? {is_perfect_score}")


# ==========================================
# 2. Inequality and Size Checks
# ==========================================
print("\n--- Basic Comparisons ---")
min_age = 18
user_age = 21

print(f"Is user allowed? (user_age >= min_age): {user_age >= min_age}")
print(f"Is user not 18? (user_age != 18):       {user_age != 18}")


# ==========================================
# 3. Chained Comparisons in Action
# ==========================================
print("\n--- Chained Comparisons ---")
safety_threshold = 25

# Checking if safety_threshold falls strictly between 10 and 50
# Python evaluates this as: (10 < safety_threshold) and (safety_threshold < 50)
is_safe = 10 < safety_threshold < 50
print(f"Is threshold within safe range? {is_safe}")

# Chaining can involve different operators too
system_status = 5
is_valid_range = 0 <= system_status != 10
print(f"Is status valid and not equal to 10? {is_valid_range}")