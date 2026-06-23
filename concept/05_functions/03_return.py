# ==========================================
# 1. Return vs. Print Demonstration
# ==========================================
def calculate_power_print(base, exponent):
    result = base ** exponent
    print(f"[Inside print function] Calculated: {result}")

def calculate_power_return(base, exponent):
    return base ** exponent

# Testing Print: The output is visible on screen, but the variable stores Nothing (None)
printed_output = calculate_power_print(2, 3)
print(f"Variable value from print function: {printed_output}") # None

# Testing Return: The output is captured in memory and can be reused in math
returned_output = calculate_power_return(2, 3)
final_calculation = returned_output * 10
print(f"Variable value from return function multiplied by 10: {final_calculation}")


# ==========================================
# 2. Multiple Values (Tuple Packing/Unpacking)
# ==========================================
print("\n--- Structural Multi-Value Packing ---")

def generate_telemetry():
    # Python implicitly packs these 3 metrics into a single tuple object
    return 200, "CONNECTED", 14.52

# Scenario A: Capturing the packed container intact
packed_tuple = generate_telemetry()
print(f"Packed Object Type: {type(packed_tuple)} | Contents: {packed_tuple}")

# Scenario B: Unpacking the values directly at the call site
status, state, latency = generate_telemetry()
print(f"Unpacked Metrics -> Status: {status} | State: {state} | Latency: {latency}ms")


# ==========================================
# 3. Early Returns Guard Pattern
# ==========================================
print("\n--- Early Return Verification ---")

def process_premium_content(user_profile):
    # Guard Layer: Early exit if unauthenticated
    if not user_profile.get("authenticated"):
        return "Access Denied: Please log in."
        
    # Guard Layer: Early exit if insufficient tier
    if user_profile.get("tier") != "premium":
        return "Access Denied: Premium subscription required."

    # Main Happy Path (Remains flat and isolated at the base level)
    print("Fetching high-bandwidth content streams...")
    return "Welcome to the Premium Dashboard Payload."

guest_user = {"authenticated": True, "tier": "free"}
print(process_premium_content(guest_user))