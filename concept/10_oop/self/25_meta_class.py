# ==========================================
# 1. THE ARCHITECTURAL METACLASS
# ==========================================

class StrictInterfaceMeta(type):
    """
    A custom metaclass that enforces strict corporate naming conventions.
    It inspects and validates the attributes of subclasses at import time.
    """
    
    # __new__ intercepts the physical creation of the Class object in memory
    def __new__(mcs, name, bases, class_dict):
        print(f"[Metaclass] Intercepting compilation of class definition structure: '{name}'")
        
        # We look through every method and attribute defined in the incoming class body
        for attribute_name, attribute_value in class_dict.items():
            # Skip standard Python internal dunder methods
            if attribute_name.startswith("__") and attribute_name.endswith("__"):
                continue
                
            # Architectural Constraint Check: Force all public methods to use snake_case
            if callable(attribute_value) and not attribute_name.islower():
                raise SystemError(
                    f"Architectural Violation: Method '{attribute_name}' inside class '{name}' "
                    f"violates system guidelines. You MUST use strict snake_case naming conventions."
                )
                
        # If all validation constraints clear safely, delegate creation back to the 'type' base engine
        return super().__new__(mcs, name, bases, class_dict)


# ==========================================
# 2. APPLYING THE METACLASS FILTER
# ==========================================
print("--- Phase 1: Importing and Loading System Layouts ---")

class CompliantService(metaclass=StrictInterfaceMeta):
    """This class compiles cleanly because its methods use snake_case rules."""
    def fetch_database_records(self):
        return "Records Retrieved"


print("\n--- Phase 2: Testing Metaclass Guardrail Failures ---")

try:
    # Defining this class will crash immediately at compile/import time, 
    # before we ever even attempt to instantiate a single object instance!
    class LegacyPaymentGateway(metaclass=StrictInterfaceMeta):
        """This class will break system compilation rules."""
        
        def processTransaction(self): # ❌ Non-compliant camelCase triggers Metaclass penalty
            return "Transaction Committed"
            
except SystemError as error:
    print(f"\n❌ Compilation Blocked Safely by Metaclass Layer:\n   {error}")