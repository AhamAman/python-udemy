# ==========================================
# 1. Mutually Exclusive Evaluation Behavior
# ==========================================
print("--- Mutual Exclusivity Demo ---")
score = 85

# Python evaluates top-to-bottom.
if score >= 70:
    print("Result: Passed with a C grade.") # Matches here! 
elif score >= 80:
    # Even though 85 >= 80 is mathematically True, Python SKIPS this block 
    # completely because the first condition already won.
    print("Result: Passed with a B grade.")
else:
    print("Result: Failed.")


# ==========================================
# 2. Independent 'if' vs. Connected 'elif'
# ==========================================
print("\n--- Independent 'if' Chain (Multiple matches can trigger) ---")
age = 22

# Independent Checks: Each one runs regardless of the others
if age >= 16:
    print("  [if] You can legally drive.")
if age >= 18:
    print("  [if] You can legally vote.")
if age >= 21:
    print("  [if] You can legally rent a car.")


print("\n--- Connected 'elif' Chain (Only the first match triggers) ---")
# Connected Checks: Only a single outcome can win
if age >= 16:
    print("  [elif] Priority tier: Teen Driver status.") # Wins and halts further checks
elif age >= 18:
    print("  [elif] Priority tier: Adult status.")
elif age >= 21:
    print("  [elif] Priority tier: Senior status.")


# ==========================================
# 3. Unlimited Multi-Branch Layout
# ==========================================
print("\n--- High Scale Branching ---")
# There is no technical limit to how many elif blocks can exist in a chain
command = "stop"

if command == "start":
    print("System initializing...")
elif command == "pause":
    print("System suspended.")
elif command == "stop":
    print("System shutting down clean.")
elif command == "restart":
    print("System recycling sockets...")
else:
    print("Command unrecognized.")