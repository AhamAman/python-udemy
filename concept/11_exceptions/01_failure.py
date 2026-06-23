import sys
import traceback

# ==========================================
# 1. UNDERSTANDING THE ERROR SPECTRUM
# ==========================================

def calculate_sensor_average(total_sum: float, count: int) -> float:
    """A simple calculation block vulnerable to runtime execution errors."""
    # Logical Error Pitfall Example: If a developer wrote '+' instead of '/',
    # it would run perfectly without crashing, but yield corrupt metrics.
    return total_sum / count


def execution_pipeline_layer_two(sum_val: float, count_val: int):
    """Middle-tier application layer forwarding arguments."""
    print("   [Layer 2] Processing pipeline metrics...")
    return calculate_sensor_average(sum_val, count_val)


def core_application_gateway(sum_val: float, count_val: int):
    """The high-level endpoint entering the system."""
    print("[Gateway] Initiating tracking matrix processing...")
    return execution_pipeline_layer_two(sum_val, count_val)


# ==========================================
# 2. EVALUATING RUNTIME HANDLED FAILURES
# ==========================================
print("--- Scenario 1: Analyzing and Reading a Runtime Traceback ---")

try:
    # Passing 0 as the denominator is grammatically valid Python code, 
    # so it passes compile time. But it blows up at runtime.
    core_application_gateway(total_sum=450.5, count_val=0)

except ZeroDivisionError as explicit_exception:
    print("\n❌ CRASH INTERCEPTED: Runtime Exception Caught.")
    print(f"Exception Type: {type(explicit_exception).__name__}")
    print(f"Exception Message: {explicit_exception}\n")
    
    print("--- LIVE TRACEBACK ANALYSIS ---")
    # We extract the stack trace format manually to inspect how Python displays it
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)


print("\n--- Scenario 2: Failures That CANNOT Be Handled ---")
# If you un-comment the code block below, the script will crash before running line 1!
# Why? Because a Syntax Error represents structurally broken grammar. 
# Python cannot compile the file into bytecode, so it never steps into the try/except block.

# try:
#     if True
#         print("Missing a colon!")
# except SyntaxError:
#     print("This block will never execute.")