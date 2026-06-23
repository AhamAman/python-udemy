# ==========================================
# 1. Defining a Function (Registration Phase)
# ==========================================
def calculate_server_uptime():
    """
    Simulates a metric calculation for infrastructure logs.
    Returns a float representing system reliability.
    """
    # This is an indented execution block
    total_hours = 720
    downtime_hours = 0.5
    uptime_percentage = ((total_hours - downtime_hours) / total_hours) * 100
    return uptime_percentage

# Notice that running this script up to here produces NO output. 
# The recipe is written, but not yet cooked.


# ==========================================
# 2. Reading Function Documentation
# ==========================================
print("--- Docstring Inspection ---")
# We can access the docstring using Python's built-in help or __doc__
print(calculate_server_uptime.__doc__)


# ==========================================
# 3. Calling a Function (Execution Phase)
# ==========================================
print("--- Control Flow Execution ---")
print("Main Program: About to call the function...")

# Calling the function pushes it onto the execution stack
current_metrics = calculate_server_uptime()

print(f"Main Program: Function has returned! Value = {current_metrics:.4f}%")


# ==========================================
# 4. Empty Functions Using 'pass'
# ==========================================
print("\n--- The Empty Placeholder ---")

def process_cloud_backup():
    # Syntactically, an empty function block will crash with an IndentationError.
    # We use 'pass' as a legal structural placeholder during development.
    pass

# Runs cleanly without doing anything
process_cloud_backup()
print("Placeholder function executed without error.")