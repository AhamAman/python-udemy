# Raw dataset: Inbound user application submissions
USER_SUBMISSIONS = [
    {"user": "alice", "score": 88, "status": "verified"},
    {"user": "bob", "score": 42, "status": "unverified"},
    {"force_drop": True}, # Corrupt edge payload
    {"user": "charlie", "score": 95, "status": "verified"}
]

# ==========================================
# 1. The Complex Single-Line Trap (Anti-Pattern)
# ==========================================
# Problem: Long, hard to scan, mixes multiple layers of filtering and structural transformation
bad_pipeline = [f"{payload['user'].upper()}::PASSED" if payload["score"] > 70 else f"{payload['user'].upper()}::FAILED" for payload in USER_SUBMISSIONS if "user" in payload if payload["status"] == "verified"]

print(f"Anti-Pattern Output: {bad_pipeline}")


# ==========================================
# 2. Refactoring Option A: Multi-Line Layout
# ==========================================
# Better: Breaking clauses onto separate lines improves scannability significantly
clean_multi_line_pipeline = [
    f"{p['user'].upper()}::PASSED" if p["score"] > 70 else f"{p['user'].upper()}::FAILED"
    for p in USER_SUBMISSIONS
    if "user" in p
    if p["status"] == "verified"
]


# ==========================================
# 3. Refactoring Option B: Helper Method Extraction (Best Practice)
# ==========================================
# Best: Isolate the business logic from the looping architecture entirely

def evaluate_submission_profile(profile: dict) -> str:
    """Pure helper function handling transformation logic clearly."""
    username = profile["user"].upper()
    if profile["score"] > 70:
        return f"{username}::PASSED"
    return f"{username}::FAILED"

# The resulting comprehension is now incredibly clean and easy to read
best_practice_pipeline = [
    evaluate_submission_profile(payload)
    for payload in USER_SUBMISSIONS
    if "user" in payload
    if payload["status"] == "verified"
]

print(f"Refactored Output:   {best_practice_pipeline}")