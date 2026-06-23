# ==========================================
# 1. Verification of Non-Leakage
# ==========================================
print("--- 1. Testing Variable Containment Boundaries ---")

# Let's ensure 'system_metric' does not exist in our global environment yet
if "system_metric" not in locals():
    print("Pre-check: 'system_metric' is completely unassigned.")

# Execute a standard list comprehension pipeline
processed_array = [system_metric * 10 for system_metric in range(1, 4)]
print(f"Pipeline Result Array: {processed_array}")

# Attempting to read 'system_metric' outside the comprehension
try:
    # In Python 2, this would print '3' (leaked value).
    # In Python 3, this crashes cleanly because the variable was contained.
    print(system_metric)
except NameError as err:
    print(f"Post-check: Caught expected NameError: {err}")
    print("-> Success: Python 3 successfully destroyed the loop variable frame.")


# ==========================================
# 2. Name Shadowing Mechanics
# ==========================================
print("\n--- 2. Trapping Name Shadowing Behavior ---")

# A pre-existing variable configuration
active_node = "CLUSTER_PRIMARY_NODE"

# Running a comprehension that reuses 'active_node' as its internal loop target identifier
node_manifest = [f"Worker-{active_node}" for active_node in [101, 102, 103]]

print(f"Comprehension Output Matrix: {node_manifest}")
# The global variable was completely shielded from the inner evaluation loop mutations:
print(f"Global 'active_node' remains untouched: {active_node}")


# ==========================================
# 3. Scope Debugging: The Enclosing Trap
# ==========================================
print("\n--- 3. Advanced Enclosing Evaluation Check ---")

def generate_multipliers():
    # An intentional architectural anti-pattern: Creating a list of functions using a comprehension
    # Because of lazy evaluation inside lambdas, they lookup 'i' when EXECUTED, not when defined.
    # By then, the comprehension loop has already ended, and 'i' cannot be found locally.
    return [lambda x: x * i for i in range(1, 4)]

factories = generate_multipliers()

# We expect factories[0](10) to be 10 * 1 = 10, factories[1](10) to be 10 * 2 = 20, etc.
# But watch what actually happens:
try:
    print(f"Factory 0 result: {factories[0](10)}")
except NameError as err:
    print(f"Caught expected Execution NameError: {err}")
    print("-> Explanation: The lambda looks for 'i' at execution time, but the comprehension's local scope is already dead!")