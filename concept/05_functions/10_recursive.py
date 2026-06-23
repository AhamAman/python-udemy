import sys

# ==========================================
# 1. Direct Linear Recursion (The Textbook Pattern)
# ==========================================
def calculate_factorial_recursive(n):
    # Pillar 1: The Base Case (The Stop Switch)
    if n <= 1:
        return 1
        
    # Pillar 2: The Recursive Case (Moving down towards the base case)
    return n * calculate_factorial_recursive(n - 1)

print("--- 1. Linear Recursion Execution ---")
# Call Stack Trace: 3 * factorial(2) -> 2 * factorial(1) -> returns 1
print(f"Factorial of 3: {calculate_factorial_recursive(3)}")


# ==========================================
# 2. Iterative Equivalent (The Memory-Safe Way)
# ==========================================
def calculate_factorial_iterative(n):
    result = 1
    # Iteration alters local registers without shifting stack frames
    for i in range(1, n + 1):
        result *= i
    return result

print("\n--- 2. Iterative Equivalent ---")
print(f"Factorial of 3 (Loop): {calculate_factorial_iterative(3)}")


# ==========================================
# 3. Indirect (Mutual) Recursion Mechanics
# ==========================================
print("\n--- 3. Indirect Recursion Wave ---")

def step_even(number):
    if number == 0:
        return True
    return step_odd(number - 1) # Passes control across boundaries to step_odd

def step_odd(number):
    if number == 0:
        return False
    return step_even(number - 1) # Passes control back to step_even

print(f"Is 4 Even? {step_even(4)}")


# ==========================================
# 4. Triggering and Inspecting the Guardrail Limit
# ==========================================
print("\n--- 4. Python Safety Limits ---")
print(f"Current System Default Recursion Limit: {sys.getrecursionlimit()}")

def broken_infinite_loop(depth):
    # Lacks a base case! Runs forever until the guardrail catches it.
    broken_infinite_loop(depth + 1)

try:
    broken_infinite_loop(depth=1)
except RecursionError as error:
    print(f"Caught expected crash: {error}")