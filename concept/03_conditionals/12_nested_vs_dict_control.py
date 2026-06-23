"""
This module demonstrates the differences, pros, cons, and performance/readability 
trade-offs between Nested If statements and Dictionary-based Control Flow (Dictionary Dispatch).
"""

# =====================================================================
# Scenario 1: Simple Mapping (Value lookup)
# Task: Determine the price of a beverage based on its size and type.
# =====================================================================

# 1A. Using Nested If/Elif
def get_price_nested_if(drink_type: str, size: str) -> float:
    drink_type = drink_type.lower()
    size = size.lower()
    
    if drink_type == "chai":
        if size == "small":
            return 10.0
        elif size == "medium":
            return 15.0
        elif size == "large":
            return 20.0
        else:
            return 0.0
    elif drink_type == "coffee":
        if size == "small":
            return 15.0
        elif size == "medium":
            return 22.0
        elif size == "large":
            return 30.0
        else:
            return 0.0
    else:
        return 0.0

# 1B. Using Dictionary-based Control (Tuple keys as a flat map)
# This eliminates nesting entirely and makes lookup O(1).
DRINK_PRICES = {
    ("chai", "small"): 10.0,
    ("chai", "medium"): 15.0,
    ("chai", "large"): 20.0,
    ("coffee", "small"): 15.0,
    ("coffee", "medium"): 22.0,
    ("coffee", "large"): 30.0,
}

def get_price_dict(drink_type: str, size: str) -> float:
    # Use .get() to handle default fallback elegantly
    return DRINK_PRICES.get((drink_type.lower(), size.lower()), 0.0)


# =====================================================================
# Scenario 2: Dynamic Execution / Action Dispatch (Dictionary of Functions)
# Task: Execute different mathematical operations.
# =====================================================================

# Helper functions
def add(a: float, b: float) -> float: return a + b
def subtract(a: float, b: float) -> float: return a - b
def multiply(a: float, b: float) -> float: return a * b
def divide(a: float, b: float) -> float: return a / b if b != 0 else float('nan')

# 2A. Using Nested/Long If-Elif Chains
def calculate_nested_if(operation: str, a: float, b: float) -> float:
    op = operation.lower()
    if op == "add" or op == "+":
        return add(a, b)
    elif op == "subtract" or op == "-":
        return subtract(a, b)
    elif op == "multiply" or op == "*":
        return multiply(a, b)
    elif op == "divide" or op == "/":
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")

# 2B. Using Dictionary Dispatch (Mapping keys to Callable functions)
# Highly extensible: adding a new operator only requires updating this dictionary.
OPERATIONS_MAP = {
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "*": multiply,
    "divide": divide,
    "/": divide
}

def calculate_dict(operation: str, a: float, b: float) -> float:
    # Retrieve the function from the dictionary, defaulting to None if not found
    func = OPERATIONS_MAP.get(operation.lower())
    if func is None:
        raise ValueError(f"Unknown operation: {operation}")
    return func(a, b)


# =====================================================================
# Summary of Trade-offs
# =====================================================================
"""
| Aspect                 | Nested If-Elif-Else                             | Dictionary-based Control                       |
|------------------------|-------------------------------------------------|-------------------------------------------------|
| Complexity             | High for deep nesting (Pyramid of Doom).        | Low. Keep code flat and readable.               |
| Speed (Scale)          | O(N) evaluation (checks sequentially).           | O(1) evaluation (hash-table lookup).            |
| Extensibility          | Hard. Requires modifying nested structures.     | Easy. Just register a new key-value pair.       |
| Complex Conditions     | Excellent (good for ranges like `x > 5`).       | Poor (mostly works for exact matches/hashes).  |
| Memory Footprint       | Negligible (just conditional checks).           | Slightly higher (allocates dictionary in RAM).  |
"""

if __name__ == "__main__":
    # Test Scenario 1
    print("--- Scenario 1: Simple Mapping ---")
    print(f"Nested If (chai, medium): {get_price_nested_if('chai', 'medium')} rupees")
    print(f"Dict Lookup (chai, medium): {get_price_dict('chai', 'medium')} rupees")
    print(f"Dict Lookup Default (unknown): {get_price_dict('matcha', 'small')} rupees")
    
    # Test Scenario 2
    print("\n--- Scenario 2: Dynamic Execution ---")
    print(f"Nested If multiply (5 * 6): {calculate_nested_if('multiply', 5, 6)}")
    print(f"Dict Dispatch multiply (5 * 6): {calculate_dict('*', 5, 6)}")
