class CombatMech:
    def __init__(mech_instance, model_name: str):
        """
        1. 'self' is NOT a protected keyword in Python!
        You can technically name it 'mech_instance', 'this', or 'dinosaur'.
        Python simply passes the new object as the first positional argument.
        (Convention dictates you should ALWAYS use 'self' to avoid confusing peers).
        """
        # Accessing instance attributes through our placeholder for self
        mech_instance.model = model_name
        mech_instance.shield_hp = 100

    def take_damage(self, amount: int):
        """Standard instance method using the idiomatic 'self' naming convention."""
        print(f"\n[Combat Log] Mech '{self.model}' hit for {amount} damage.")
        
        # Without writing 'self.', Python would search for a local variable inside 
        # this function scope and fail. 'self.' targets the object's unique __dict__.
        self.shield_hp -= amount
        print(f"             Shield integrity now at: {self.shield_hp}%")


# ==========================================
# RUNNING THE MECHANICS EXPERIMENT
# ==========================================
print("--- Phase 1: Object Instantiation ---")

# We create a mech. Python allocates memory for it.
gundam = CombatMech("RX-78-2")
print(f"The unique memory address of our object 'gundam' is: {hex(id(gundam))}")


print("\n--- Phase 2: Automatic vs. Explicit Passing ---")

# Approach A: The standard way (Automatic passing)
# Notice we pass only ONE argument (amount=30), but the definition requires two (self, amount).
gundam.take_damage(30)

# Approach B: The raw, under-the-hood way (Explicit passing)
# This proves exactly what Python translates Approach A into. 
# We call the function directly from the Class and pass the instance into 'self' manually.
print("\nExecuting explicit class-level invocation...")
CombatMech.take_damage(gundam, 40)


print("\n--- Phase 3: Beginner Pitfalls & Scope ---")

class BrokenMech:
    def __init__(self, model_name: str):
        # Mistake 1: Forgetting 'self.' creates a temporary local variable 
        # that vanishes as soon as __init__ finishes executing!
        local_model = model_name 
        self.actual_model = model_name

    def display(self):
        try:
            # This will crash because 'local_model' wasn't bound to the object via self
            print(f"Model: {self.local_model}")
        except AttributeError as e:
            print(f"❌ AttributeError Caught: {e}")
            print(f"   Correctly bound variable works: '{self.actual_model}'")

broken = BrokenMech("Zaku-II")
broken.display()