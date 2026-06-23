# Raw telemetry: Server nodes with their current temperature metrics
SERVER_TEMPS = [
    {"node": "Node_A", "temp": 32},
    {"node": "Node_B", "temp": 76},
    {"node": "Node_C", "temp": 55},
    {"node": "Node_D", "temp": 91}
]

# ==========================================
# 1. Standard Transformation (if-else)
# ==========================================
print("--- 1. Basic In-Line Transformation ---")

# Task: Label each node as "CRITICAL" if temp > 70, otherwise label it "NORMAL"
# Notice that no nodes are dropped; we are transforming the strings inline.
status_manifest = [
    f"{n['node']}: CRITICAL" if n["temp"] > 70 else f"{n['node']}: NORMAL"
    for n in SERVER_TEMPS
]
print(f"Status Manifest: {status_manifest}")


# ==========================================
# 2. Nested Multi-Tier Ternary (The Trap)
# ==========================================
print("\n--- 2. Nested Inline Conditions ---")

# Task: Categorize status tiers: > 80 -> RED, > 50 -> YELLOW, otherwise GREEN
# This structure is dense, hard to scan, and prone to syntax errors.
color_alerts = [
    "RED" if n["temp"] > 80 else "YELLOW" if n["temp"] > 50 else "GREEN"
    for n in SERVER_TEMPS
]
print(f"Inline Nested Colors: {color_alerts}")


# ==========================================
# 3. Clean Refactoring (The Production Pattern)
# ==========================================
print("\n--- 3. Refactored Helper Pattern ---")

# Step A: Encapsulate the messy conditional logic inside a clean, typed pure function
def determine_node_alert_color(temperature: int) -> str:
    """Cohesive mapping helper that replaces unreadable nested ternary logic."""
    if temperature > 80:
        return "RED"
    if temperature > 50:
        return "YELLOW"
    return "GREEN"

# Step B: Deploy the helper function inside the comprehension expression slot
clean_color_alerts = [determine_node_alert_color(n["temp"]) for n in SERVER_TEMPS]
print(f"Refactored Clean Colors: {clean_color_alerts}")


# ==========================================
# 4. Common Mistake: Mixing Trailing Filters with Front Transforms
# ==========================================
print("\n--- 4. Combining Filters and Transforms ---")

# Task: For ONLINE nodes (temp > 0), mark as HIGH if temp > 60, else LOW.
# Here, we combine a FRONT transformation with a TAIL filter smoothly.
mixed_results = [
    "HIGH" if n["temp"] > 60 else "LOW"
    for n in SERVER_TEMPS
    if n["temp"] > 35  # Tail filter discards Node_A (32) entirely from the pipeline
]
print(f"Filtered + Transformed Output: {mixed_results}")