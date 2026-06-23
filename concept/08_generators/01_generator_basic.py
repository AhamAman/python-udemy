# ==========================================
# 1. Defining the Generator Architecture
# ==========================================
def production_line_generator():
    """A clear state machine trace using the yield keyword."""
    print("  [GEN ENGINE] -> Step 1 initialization started...")
    local_state_counter = 100
    
    yield f"Payload Alpha (State Tracker: {local_state_counter})"
    
    # When resumed, local_state_counter is still perfectly preserved in memory
    print("  [GEN ENGINE] -> Step 2 resuming execution flow...")
    local_state_counter += 50
    
    yield f"Payload Beta (State Tracker: {local_state_counter})"
    
    print("  [GEN ENGINE] -> Cleaning up stream frames...")
    # The function ends here, implicitly triggering a StopIteration exception


# ==========================================
# 2. Manual Consumption via next()
# ==========================================
print("--- Scenario A: Manual next() Inspection ---")

# Step A: Instantiate the generator. Notice no print statements execute yet.
factory_stream = production_line_generator()
print(f"Returned object signature: {factory_stream}")

# Step B: Push to the first yield point
print("\nTriggering next() #1:")
item_1 = next(factory_stream)
print(f"Consumer Received: '{item_1}'")

# Step C: Push to the second yield point
print("\nTriggering next() #2:")
item_2 = next(factory_stream)
print(f"Consumer Received: '{item_2}'")

# Step D: Force exhaustion check
print("\nTriggering next() #3 (Expecting Stream Exhaustion):")
try:
    next(factory_stream)
except StopIteration:
    print("Caught expected StopIteration Exception. The stream is safely closed.")


# ==========================================
# 3. Clean Loop Consumption
# ==========================================
print("\n--- Scenario B: Clean Loop Consumption ---")

# Re-instantiate a fresh, un-exhausted generator instance
fresh_stream = production_line_generator()

# The for loop automatically handles calling next() and intercepting StopIteration safely
for payload in fresh_stream:
    print(f"Loop Consumer Intercepted: {payload}")