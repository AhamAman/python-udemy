def execute_system_calculation(denominator: float):
    print(f"\n>>> Executing application layer logic with denominator: {denominator}")
    try:
        if denominator < 0:
            # When we 'raise', we are explicitly instantiating an exception object.
            # The string passed inside the parentheses becomes the exception message.
            raise ValueError("Boundary Violation: System values cannot be negative.", 400, "CRITICAL")
            
        result = 1000 / denominator
        print(f"   [Success] Outcome: {result}")

    # ==========================================
    # CAPTURING THE EXCEPTION INSTANCE
    # ==========================================
    # The 'as error' syntax grabs the live object instance thrown by the system
    # and binds it to a local variable named 'error'.
    except ValueError as error:
        print("\n❌ Intercepted ValueError Object!")
        
        # 1. String Representation of Exceptions
        # Printing or calling str(error) extracts the primary message string.
        print(f"   ↳ Direct String View: '{error}'")
        
        # 2. Inspecting the 'args' Attribute
        # All arguments passed to an exception during creation are saved into a tuple called 'args'.
        print(f"   ↳ Object Args Tuple:  {error.args}")
        print(f"   ↳ Primary Message:    {error.args[0]}")
        print(f"   ↳ Custom Status Code: {error.args[1] if len(error.args) > 1 else 'N/A'}")
        
        # 3. Class Introspection
        # Since it is an object, we can verify its exact class identity
        print(f"   ↳ Exact Class Type:   {error.__class__.__name__}")

    except ZeroDivisionError as error:
        print("\n❌ Intercepted ZeroDivisionError Object!")
        # Built-in exceptions also use the args tuple to pass their messages down
        print(f"   ↳ Default Engine Message: '{error}'")
        print(f"   ↳ Under-the-hood tracebacks exist on the object attribute: {error.__traceback__}")


# ==========================================
# EXECUTING INTROSPECTION RUNS
# ==========================================
# Triggering our custom raised exception with extra meta arguments
execute_system_calculation(denominator=-5.0)

# Triggering a built-in math exception engine
execute_system_calculation(denominator=0.0)