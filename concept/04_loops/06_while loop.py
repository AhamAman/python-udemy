import random
import time

# =====================================================================
# 1. THE STANDARD COUNTER (Preventing Infinite Loops)
# =====================================================================
print("--- 1. Controlled Counter Loop ---")

counter = 1  # 1. Initial State

while counter <= 3:  # 2. The Condition
    print(f"Loop cycle: {counter}")
    counter += 1  # 3. State Update (Without this, it's an infinite loop!)

print("Loop finished safely.\n")


# =====================================================================
# 2. INPUT-DRIVEN LOOP WITH A SENTINEL VALUE
# =====================================================================
print("--- 2. Input-driven Loop with Sentinel ---")

# We mock user input for demonstration purposes
mock_inputs = ["hello", "continue", "quit", "never_reached"]
input_iterator = iter(mock_inputs)

sentinel = "quit"
user_input = ""

while user_input != sentinel:
    # Simulating asking a user for input
    user_input = next(input_iterator)
    print(f"User entered: '{user_input}'")
    
    if user_input == sentinel:
        print("Sentinel value detected! Exiting.")

print("Program successfully shut down.\n")


# =====================================================================
# 3. EVENT-DRIVEN LOOP
# =====================================================================
print("--- 3. Event-Driven Loop (Simulating a Battery Charge) ---")

battery_level = 85
is_fully_charged = False  # Event flag

while not is_fully_charged:
    print(f"Charging... Current battery: {battery_level}%")
    
    # Simulate an external event changing the state
    battery_level += random.randint(5, 10)
    
    # Check if the termination event condition is met
    if battery_level >= 100:
        battery_level = 100
        is_fully_charged = True

print(f"Event triggered! Final Battery: {battery_level}%. Disconnecting charger.")