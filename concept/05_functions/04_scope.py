# ==========================================
# 1. Global Scope Initialization
# ==========================================
system_status = "OPERATIONAL"  # Global Variable
user_count = 100               # Global Variable

# ==========================================
# 2. Variable Shadowing Demo
# ==========================================
def process_local_metrics():
    # Shadowing: This creates an isolated local 'system_status'.
    # It does NOT overwrite the global variable outside.
    system_status = "MAINTENANCE"
    local_worker_id = "Worker_99" # Local Variable
    
    print("--- Inside Local Function Scope ---")
    print(f"Local system_status:  {system_status}")  # Reads Local (Shadowed)
    print(f"Can read global count: {user_count}")     # Falls through LEGB to read Global


process_local_metrics()

print("\n--- Back in Global Scope ---")
print(f"Global system_status remains: {system_status}")

try:
    # This will crash because local_worker_id was destroyed with the function stack frame
    print(local_worker_id)
except NameError as err:
    print(f"Caught expected NameError: {err}")


# ==========================================
# 3. Modifying Global Scope cleanly vs dangerously
# ==========================================
print("\n--- Modifying Global Variables ---")

def unsafe_global_mutation():
    global user_count  # Explicitly hijacking the global namespace rule
    user_count += 1    # Directly mutates the global variable in RAM

unsafe_global_mutation()
print(f"Global user_count after modification: {user_count}")


# ==========================================
# 4. The UnboundLocalError Trap
# ==========================================
print("\n--- The UnboundLocalError Trap ---")
alert_level = "LOW"

def trigger_alert_trap():
    try:
        # Python scans the function block BEFORE running it. 
        # Because it sees 'alert_level =' down on line 56, it marks 'alert_level' 
        # as a local variable for this entire block.
        # Therefore, trying to print it on line 55 crashes because the local variable 
        # hasn't been initialized yet!
        print(alert_level) 
        alert_level = "CRITICAL"
    except UnboundLocalError as err:
        print(f"Caught expected UnboundLocalError: {err}")

trigger_alert_trap()

