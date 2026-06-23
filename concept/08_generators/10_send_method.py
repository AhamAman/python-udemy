def dynamic_counter():
    print("[Gen] Starting...")
    count = 0
    
    while True:
        # 1. We yield 'count' OUT, and pause.
        # 2. When revived via .send(), the incoming value is assigned to 'external_jump'
        external_jump = yield count 
        
        if external_jump is not None:
            print(f"[Gen] 📥 State Modified! Jumping from {count} to {external_jump}")
            count = external_jump
        else:
            print("[Gen] 🔄 No input received. Incrementing normally.")
            count += 1

# --- Execution ---
gen = dynamic_counter()

# Step 1: The Priming Rule
# You cannot send data to a generator that hasn't started yet.
# next(gen) advances execution to the very first `yield`.
first_val = next(gen) 
print(f"Caller received: {first_val}") # Outputs: 0

# Step 2: Normal Advance
# Calling next(gen) is exactly equivalent to calling gen.send(None).
second_val = next(gen)
print(f"Caller received: {second_val}") # Outputs: 1

# Step 3: State Modification via .send()
# We inject '50' directly into the paused yield statement.
third_val = gen.send(50)
print(f"Caller received: {third_val}") # Outputs: 50