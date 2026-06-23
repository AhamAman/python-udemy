# ==========================================
# 1. Standard LEGB Layers in Action
# ==========================================
import builtins

# Global Scope (G)
message = "Global Text Data"

def outer_function():
    # Enclosing Scope (E)
    message = "Enclosing Text Data"
    
    def inner_function():
        # Local Scope (L)
        # Un-commenting the line below forces Python to stop at the Local (L) tier:
        # message = "Local Text Data"
        
        print("--- LEGB Lookup ---")
        print(f"Resolved message: {message}") # Traverses L -> E (Matches Enclosing!)
        
    inner_function()

outer_function()


# ==========================================
# 2. Modifying Enclosing Scope via nonlocal
# ==========================================
print("\n--- Nonlocal State Mutation ---")

def step_counter_engine():
    steps = 0  # Enclosing Variable
    
    def increment():
        nonlocal steps  # Overrides safety; points directly to Enclosing layer
        steps += 1
        return steps
        
    return increment

# Instantiate a closure profile
track_run = step_counter_engine()
print(f"Step 1: {track_run()}")
print(f"Step 2: {track_run()}")


# ==========================================
# 3. Common Debugging / Pitfall Scenarios
# ==========================================
print("\n--- Scope Error Traps ---")

# Scenario A: Shadowing / Overwriting Built-ins (Dangerous!)
# Never name a variable 'sum', 'list', or 'str'
sum = 10 + 20 # Overwrites the built-in sum() function in the global namespace

try:
    # Trying to use the built-in function now crashes because Python stops at the Global variable 'sum'
    calculate = sum([5, 5, 5])
except TypeError as err:
    print(f"Caught expected Shadowing Error: {err}")

# Cleaning up the global namespace namespace trap
del sum 


# Scenario B: UnboundLocalError Trap (Read-before-write)
score = 100

def modify_score_trap():
    try:
        # Python compiles this block and marks 'score' as local because of the assignment down below.
        # Therefore, trying to read it here fails because it doesn't exist *locally* yet.
        print(score) 
        score = 200
    except UnboundLocalError as err:
        print(f"Caught expected UnboundLocalError: {err}")

modify_score_trap()