# ==========================================
# 1. Defining Parameters (The Blueprint)
# ==========================================
# Rule Check: Required parameters (username, IP) come BEFORE optional ones (port)
def connect_to_node(username, network_ip, port=22):
    """
    Simulates a secure network connection profile.
    'username' and 'network_ip' are REQUIRED parameters.
    'port' is an OPTIONAL parameter with a default value of 22.
    """
    print(f"Connecting user '{username}' to target host [{network_ip}] on port {port}...")
    return True


# ==========================================
# 2. Argument Passing Strategies (The Deliveries)
# ==========================================
print("--- Positional Assignment ---")
# Order matters perfectly here
connect_to_node("admin_dev", "192.168.1.105")

print("\n--- Keyword Assignment ---")
# Explicit parameter names bypass positional layout limits entirely
connect_to_node(network_ip="10.0.0.1", username="security_bot")

print("\n--- Overriding Defaults ---")
# Providing an argument for the optional port parameter replaces the default 22
connect_to_node("root_user", "127.0.0.1", port=8080)


# ==========================================
# 3. Mixing and Syntax Failures
# ==========================================
print("\n--- Mixed Layout Verification ---")
# Valid Mixed Call: Positional first, Keyword second
connect_to_node("guest_user", network_ip="192.168.1.1")

# Invalid Mixed Call: Triggering SyntaxError simulation
try:
    exec("""
# This fails instantly because a positional argument follows a keyword argument
connect_to_node(username="hacker", "192.168.1.5")
    """)
except SyntaxError as err:
    print(f"Caught expected SyntaxError: {err}")

# Invalid Signature Definition: Triggering Signature Syntax Error
try:
    exec("""
# This fails because a required parameter follows an optional default one
def bad_signature(timeout=5, host):
    pass
    """)
except SyntaxError as err:
    print(f"Caught expected Signature Compilation Error: {err}")