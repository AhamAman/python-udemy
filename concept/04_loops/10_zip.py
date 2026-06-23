import itertools

def separator(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Sample Data
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
roles = ["Dev", "Design", "Ops"]

# =====================================================================
# 1. ITERATING MULTIPLE COLLECTIONS
# =====================================================================
separator("1. Standard zip() Iteration")

# zip() pairs names and scores element-by-element
for name, score in zip(names, scores):
    print(f"Student: {name} | Score: {score}")

# You can zip more than two collections at once
print("\nZipping three collections:")
for name, score, role in zip(names, scores, roles):
    print(f"Employee: {name} ({role}) scored {score}")


# =====================================================================
# 2. UNEQUAL LENGTH COLLECTIONS
# =====================================================================
separator("2. Handling Mismatched Lengths")

short_list = ["Apple", "Banana"]
long_list = [10, 20, 30, 40]

# Standard zip() stops at the SHORTEST iterable (it truncates the rest)
print("Standard zip() on mismatched lengths (truncates):")
for item, count in zip(short_list, long_list):
    print(f"  {item}: {count}")


# =====================================================================
# 3. ZIP_LONGEST()
# =====================================================================
separator("3. Using itertools.zip_longest()")

# zip_longest keeps going until the LONGEST iterable is exhausted
# It fills missing values with a placeholder (defaults to None)
print("zip_longest with default None:")
for item, count in itertools.zip_longest(short_list, long_list):
    print(f"  {item}: {count}")

print("\nzip_longest with custom fillvalue:")
for item, count in itertools.zip_longest(short_list, long_list, fillvalue="Out of Stock"):
    print(f"  {item}: {count}")


# =====================================================================
# 4. COMMON USE CASES
# =====================================================================
separator("4. Real-World Applications")

# Use Case A: Creating Dictionaries quickly
# Merging keys and values into a hash map instantly
user_dict = dict(zip(names, roles))
print(f"A. Dictionary Creation:\n   {user_dict}")

# Use Case B: Unzipping Data
# You can unpack a zipped object back into separate collections using the * operator
paired_data = [("A", 1), ("B", 2), ("C", 3)]
letters, numbers = zip(*paired_data)
print(f"\nB. Unzipping data back into tuples:\n   Letters: {letters}\n   Numbers: {numbers}")

# Use Case C: Parallel Processing Validation
# Checking if corresponding items meet a criteria
thresholds = [80, 90, 80]
print("\nC. Parallel Condition Evaluation:")
for name, score, threshold in zip(names, scores, thresholds):
    passed = "YES" if score >= threshold else "NO"
    print(f"   Did {name} pass threshold ({threshold})? {passed}")

separator("Execution Complete")