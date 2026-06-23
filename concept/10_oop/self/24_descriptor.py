class NonNegativeNumber:
    """
    A Descriptor that enforces numerical boundaries.
    This acts as a reusable attribute controller.
    """
    def __init__(self, storage_name: str):
        # We must give the descriptor a unique key name to store its data 
        # inside the host instance's __dict__.
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        """
        Triggered when reading the attribute.
        instance: The object calling the attribute (e.g., rocket_booster).
        owner: The class type of the instance (e.g., RocketBooster).
        """
        if instance is None:
            # If called from the Class namespace directly (RocketBooster.thrust)
            return self
        
        print(f"   [Descriptor __get__] Fetching values for key: '{self.storage_name}'")
        return instance.__dict__.get(self.storage_name, 0.0)

    def __set__(self, instance, value):
        """Triggered when writing/modifying the attribute."""
        print(f"   [Descriptor __set__] Intercepting write request -> {self.storage_name} = {value}")
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"Property '{self.storage_name}' requires numerical inputs.")
            
        if value < 0:
            raise ValueError(f"Boundary Violation: '{self.storage_name}' cannot be negative.")
            
        # Crucial Design Pattern: Store the data directly in the HOST object's __dict__
        # to ensure separate data separation across multiple instances.
        instance.__dict__[self.storage_name] = float(value)


# ==========================================
# HOUSING THE DESCRIPTOR WITHIN A DATA CLASS
# ==========================================

class RocketBooster:
    # We instantiate our descriptors directly at the class level.
    # They act as intelligent gatekeepers for incoming attributes.
    thrust = NonNegativeNumber(storage_name="booster_thrust")
    fuel_mass = NonNegativeNumber(storage_name="booster_fuel_mass")

    def __init__(self, name: str, initial_thrust: float, initial_fuel: float):
        self.name = name
        # These operations automatically fire the descriptor's __set__ loops
        self.thrust = initial_thrust
        self.fuel_mass = initial_fuel


# ==========================================
# RUNNING THE PIPELINE DESCRIPTOR INTERFACE
# ==========================================
print("--- Phase 1: Successful Instantiation & Isolation ---")

booster_alpha = RocketBooster("Alpha-Heavy", initial_thrust=1500.0, initial_fuel=450.0)
booster_beta  = RocketBooster("Beta-Scout", initial_thrust=200.0, initial_fuel=80.0)

print(f"\nBooster Alpha Snapshot Readout:")
# Fires __get__ underneath
print(f"   Thrust: {booster_alpha.thrust} kN | Fuel: {booster_alpha.fuel_mass} kg")


print("\n--- Phase 2: Evaluating Local Memory Structures ---")
# To prove the descriptor stores values safely on the individual instances:
print(f"Booster Alpha Dictionary State: {booster_alpha.__dict__}")
print(f"Booster Beta Dictionary State:  {booster_beta.__dict__}")


print("\n--- Phase 3: Defensive Boundary Violations ---")
try:
    print("\nAttempting to inject a negative vector threshold...")
    booster_alpha.thrust = -45.2
except ValueError as e:
    print(f"❌ Operation Safely Blocked by Descriptor Engine: {e}")