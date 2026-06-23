# ==========================================
# 1. Operator Precedence Trap
# ==========================================
print("--- Precedence vs Parentheses ---")
has_ticket = False
is_admin = True
system_active = False

# Standard Precedence Order: 'not' goes first, then 'and', then 'or'
# Expanded steps:
# 1. not system_active -> True
# 2. is_admin and True  -> True
# 3. has_ticket or True -> True
result_precedence = has_ticket or is_admin and not system_active
print(f"Standard Evaluation Result: {result_precedence}") # Outputs: True

# Forcing a structural change using parentheses
# Python is forced to evaluate the 'or' gate first
result_forced = (has_ticket or is_admin) and not system_active
print(f"Parentheses Forced Result:  {result_forced}")    # Outputs: False


# ==========================================
# 2. Short-Circuiting as a Safety Guardrail
# ==========================================
print("\n--- Short-Circuit Safety Guardrails ---")
items = []

# If 'items' is empty, it is Falsy. 
# 'if items' fails -> Python short-circuits and NEVER executes items[0].
# This single line safely avoids an IndexError crash!
if items and items[0] == "secret_key":
    print("Access Granted.")
else:
    print("Safely skipped check without crashing.")


# ==========================================
# 3. The Dangerous Side-Effect Bug Trap
# ==========================================
print("\n--- The Short-Circuit Side-Effect Trap ---")
state_counter = 0

def increment_system_counter():
    global state_counter
    state_counter += 1
    return True

# Scenario A: Left side is True in an OR expression
# Python hits 'True', knows the whole condition is True, and skips the function completely!
if True or increment_system_counter():
    print(f"Branch executed. Counter state: {state_counter} <- (Bug! It didn't increment!)")

# Scenario B: Left side is False in an OR expression
# Python is forced to evaluate the right side to determine the answer.
if False or increment_system_counter():
    print(f"Branch executed. Counter state: {state_counter} <- (Function actually ran.)")