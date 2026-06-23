"""
UNDERSTANDING FUNCTION OBJECTS IN PYTHON

Core Axiom: Everything in Python is an object. 
A function is not just a block of executable code; it is a live instance 
of the 'function' class living on the heap.
"""

import types

# -----------------------------------------------------------------
# 1. The Target Function
# -----------------------------------------------------------------
def greet(name: str) -> str:
    """Return a friendly, customized greeting."""
    return f"Hello, {name}!"


# -----------------------------------------------------------------
# 2. Custom Callable Class
# -----------------------------------------------------------------
class StatefulMultiplier:
    """An object instance that behaves like a function by implementing __call__."""
    def __init__(self, factor: int):
        self.factor = factor

    def __call__(self, value: int) -> int:
        # This magic method turns instances of this class into 'callables'
        return value * self.factor


# ============================================================================
# EXECUTION PIPELINE
# ============================================================================

if __name__ == "__main__":
    print("--- 1. Identity, Types & Aliasing ---")
    # A function has an address, a type, and can be pointed to by variables
    print(f"Type of 'greet': {type(greet)}") 
    print(f"Memory address (id): {id(greet)}")
    
    # Assigning the function object to a new variable (no parentheses!)
    say_hi = greet
    print(f"Are 'say_hi' and 'greet' the exact same object? {say_hi is greet}")
    print(f"Executing via alias: {say_hi('Alice')}")

    print("\n--- 2. Inspecting Function Object Metadata ---")
    # Because it is an object, it has properties we can read at runtime
    print(f"Function Name (__name__): {greet.__name__}")
    print(f"Docstring (__doc__): {greet.__doc__.strip()}")
    print(f"Type Hints (__annotations__): {greet.__annotations__}")
    
    # Diving into the compiled bytecode metadata container
    print(f"Expected Argument Count (__code__.co_argcount): {greet.__code__.co_argcount}")
    print(f"Variable names inside scope (__code__.co_varnames): {greet.__code__.co_varnames}")

    print("\n--- 3. First-Class Citizenry: Collections & Arguments ---")
    # A. Storing functions inside data structures
    math_pipeline = [
        lambda x: x + 10,
        lambda x: x * 2,
        lambda x: x - 5
    ]
    
    value = 10
    print(f"Starting value: {value}")
    for transform in math_pipeline:
        value = transform(value)  # Executing each function object in sequence
        print(f"👉 After {transform.__name__}: {value}")

    # B. Passing a function as an argument (Higher-Order Function)
    def telemetry_wrapper(func, argument):
        print(f"[Telemetry] Executing function '{func.__name__}' dynamically...")
        return func(argument)

    print(telemetry_wrapper(greet, "Bob"))

    print("\n--- 4. First-Class Citizenry: Returning Functions (Factories) ---")
    # C. Returning a function object from another function
    def power_factory(exponent):
        def power(base):
            return base ** exponent  # Closes over 'exponent' from outer scope
        return power  # Returning the function object itself

    cube = power_factory(3)
    print(f"Type of 'cube': {type(cube)}")
    print(f"Execution of generated factory function (2^3): {cube(2)}")

    print("\n--- 5. Custom Callable Objects ---")
    # Instances of classes that implement __call__ can masquerade as functions
    triple = StatefulMultiplier(factor=3)
    
    print(f"Is 'triple' an instance of StatefulMultiplier? {isinstance(triple, StatefulMultiplier)}")
    print(f"Executing 'triple' object directly: {triple(10)}")  # 10 * 3 = 30

    print("\n--- 6. Checking 'Callability' ---")
    # The built-in callable() function checks if an object supports parentheses execution
    print(f"Is 'greet' (function) callable? {callable(greet)}")
    print(f"Is 'triple' (class instance) callable? {callable(triple)}")
    print(f"Is a raw string ('hello') callable? {callable('hello')}")