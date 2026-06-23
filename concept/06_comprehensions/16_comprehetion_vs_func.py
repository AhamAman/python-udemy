from functools import reduce

# Raw dataset representing production system profiles
USER_PROFILES = [
    {"user": "alex",   "score": 45, "tier": "standard"},
    {"user": "morgan", "score": 82, "tier": "premium"},
    {"user": "taylor", "score": 91, "tier": "premium"},
    {"user": "jordan", "score": 15, "tier": "free"}
]

# ==========================================
# Paradigm A: Built-in Functional Primitives
# ==========================================
print("--- Paradigm A: Map, Filter, and Reduce ---")

# Step 1: Filter out premium tier users only
premium_iter = filter(lambda u: u["tier"] == "premium", USER_PROFILES)

# Step 2: Map/extract scores from the filtered records
scores_iter = map(lambda u: u["score"], premium_iter)

# Step 3: Reduce scores array to calculate total cumulative credit metrics
# reduce() eagerly consumes the lazy iterator stream to compute a single scalar value
total_functional_score = reduce(lambda running_sum, score: running_sum + score, scores_iter, 0)

print(f"Aggregated Score via Functional Primitives: {total_functional_score}")


# ==========================================
# Paradigm B: Declarative Comprehension Pipelines
# ==========================================
print("\n--- Paradigm B: Inline Comprehension Mapping ---")

# Task: Achieve the exact same ETL pipeline structure cleanly using a comprehension.
# A list comprehension maps and filters in a single pass, which we feed to sum().
total_comprehension_score = sum(
    [u["score"] for u in USER_PROFILES if u["tier"] == "premium"]
)

print(f"Aggregated Score via Comprehension:         {total_comprehension_score}")


# ==========================================
# Paradigm C: Memory-Safe Generator Pipelines
# ==========================================
print("\n--- Paradigm C: Lazy Generator Pipeline ---")

# Best Practice optimization: Swapping square brackets for parentheses
# gives us the memory safety of map/filter with the clean readability of a comprehension.
lazy_score_pipeline = (u["score"] for u in USER_PROFILES if u["tier"] == "premium")

print(f"Lazy Stream Proxy Pointer: {lazy_score_pipeline}")
print(f"Final Aggregation Output:  {sum(lazy_score_pipeline)}")