# ==========================================
# 1. THE PARENT CLASS (The Foundation)
# ==========================================
class CommercialVessel:
    """Represents the foundational blueprint for all maritime ships."""
    
    def __init__(self, vessel_name: str, max_speed_knots: float):
        self.name = vessel_name
        self.max_speed = max_speed_knots
        self.is_anchored = True

    def weigh_anchor(self):
        """Shared behavior inherited by all child classes automatically."""
        self.is_anchored = False
        print(f"[{self.name}] Anchor raised. Ready for navigation.")

    def calculate_transit_time(self, nautical_miles: float) -> float:
        """Shared utility computation."""
        return nautical_miles / self.max_speed


# ==========================================
# 2. THE CHILD CLASS (Specialization)
# ==========================================
# By passing 'CommercialVessel' inside parentheses, we establish inheritance.
class CargoContainerShip(CommercialVessel):
    """A specialized child class inheriting from CommercialVessel."""

    def __init__(self, vessel_name: str, max_speed_knots: float, total_slots: int):
        # 1. CALLING PARENT METHODS via super()
        # super() looks up the inheritance chain to execute the parent's __init__.
        # This prevents rewriting variable assignments like 'self.name = vessel_name'.
        super().__init__(vessel_name, max_speed_knots)
        
        # 2. EXTENDING PARENT BEHAVIOR
        # Child-specific attributes that the parent class knows nothing about
        self.max_container_slots = total_slots
        self.loaded_containers = 0

    def load_cargo(self, manifest_count: int):
        """Extended behavior unique to this child subclass."""
        if self.loaded_containers + manifest_count <= self.max_container_slots:
            self.loaded_containers += manifest_count
            print(f"[{self.name}] Successfully loaded {manifest_count} containers.")
        else:
            print(f"[{self.name}] ❌ Loading Failed: Exceeds capacity constraints.")

    # 3. OVERRIDING METHODS
    # We redefine a method completely to replace the generic behavior 
    # defined in the parent class with specialized child-level logic.
    def weigh_anchor(self):
        """Overrides the parent's weigh_anchor method to add cargo safety protocols."""
        if self.loaded_containers == 0:
            print(f"[{self.name}] Safety Warning: Vessel is unweighted. Checking ballast pumps...")
            
        # We can still invoke the parent's original behavior inside our override!
        super().weigh_anchor()


# ==========================================
# 3. RUNNING THE INHERITANCE SYSTEM
# ==========================================
print("--- Phase 1: Instantiating the Child Class ---")

# cargo_ship receives Parent arguments AND Child arguments
cargo_ship = CargoContainerShip(vessel_name="Pacific Horizon", max_speed_knots=22.0, total_slots=5000)

print(f"Vessel Class Type: {type(cargo_ship)}")
print(f"Inherited Name Attribute: {cargo_ship.name}")
print(f"Child-Specific Cargo Capacity: {cargo_ship.max_container_slots} slots")


print("\n--- Phase 2: Utilizing Inherited and Extended Behavior ---")

# Accessing a method defined strictly on the child class
cargo_ship.load_cargo(1200)

# Accessing a method defined strictly on the parent class (Code Reuse)
hours_needed = cargo_ship.calculate_transit_time(nautical_miles=440.0)
print(f"Calculated voyage transit time: {hours_needed:.1f} hours")


print("\n--- Phase 3: Triggering Overridden Logic ---")

# This calls the child's overridden version of the method, not the parent's generic version
cargo_ship.weigh_anchor()