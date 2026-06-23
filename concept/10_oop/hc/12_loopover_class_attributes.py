import types

class Chai:
    temperature = "Hot"
    strength = "Strong"
    origin = "Assam"

    def brew(self):
        print("Brewing some delicious chai...")

def get_custom_class_attributes(cls):
    """
    Extracts and returns only user-defined data attributes from a class,
    filtering out magic methods, private internals, and functions.
    """
    custom_attributes = {}
    
    for key, value in vars(cls).items():
        # 1. Filter out private/magic attributes (starting with '_')
        # 2. Filter out actual functions, methods, or built-in functions
        if not key.startswith('_') and not isinstance(value, (types.FunctionType, types.MethodType, type)):
            custom_attributes[key] = value
            
    return custom_attributes

# --- Execution ---

# 1. Get the filtered attributes dictionary
chai_menu = get_custom_class_attributes(Chai)

# 2. Loop over them cleanly
print("--- Chai Class Custom Attributes ---")
for attribute, value in chai_menu.items():
    print(f"{attribute.capitalize()}: {value}")