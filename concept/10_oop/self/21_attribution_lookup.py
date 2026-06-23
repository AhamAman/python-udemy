class AutonomousCore:
    # Class Attribute
    system_status = "Online"
    firmware_version = 1.0

    def __init__(self, core_id: str):
        # Instance Attribute
        self.core_id = core_id


class DroneUnit(AutonomousCore):
    # Overriding class attribute locally in the child class
    firmware_version = 2.4
    
    def __init__(self, core_id: str, payload_type: str):
        super().__init__(core_id)
        self.payload = payload_type


# ==========================================
# EXECUTING LOOKUP INTROSPECTION
# ==========================================
print("--- Phase 1: Direct Dictionary Mapping ---")

scout_drone = DroneUnit(core_id="DRN-88", payload_type="Thermal Cam")

# Every object stores its local state in a raw dictionary called __dict__
print(f"Scout Instance __dict__: {scout_drone.__dict__}")
print(f"DroneUnit Class __dict__ Keys: {list(DroneUnit.__dict__.keys())}")
print(f"AutonomousCore Class __dict__ Keys: {list(AutonomousCore.__dict__.keys())}")


print("\n--- Phase 2: Walking the Resolution Path ---")

# Lookup 1: Local Instance Space
# Python instantly finds 'payload' in the scout_drone.__dict__
print(f"1. Fetching 'payload': {scout_drone.payload}")

# Lookup 2: Immediate Class Space
# Python checks scout_drone.__dict__ (fails), climbs to DroneUnit.__dict__ (finds 2.4)
print(f"2. Fetching 'firmware_version': {scout_drone.firmware_version}")

# Lookup 3: Parent Class Space via MRO
# Python checks instance (fails) -> DroneUnit (fails) -> AutonomousCore (finds 'Online')
print(f"3. Fetching 'system_status': {scout_drone.system_status}")


print("\n--- Phase 3: The Pitfall of Attribute Shadowing ---")

# Let's write an assignment that mimics a class variable change
scout_drone.system_status = "Degraded" 

# What happened under the hood?
print(f"Scout Instance __dict__ now looks like: {scout_drone.__dict__}")
print(f"Scout Current View: {scout_drone.system_status}")

# The class level remains completely unaltered because lookup checks the instance first!
print(f"Global Core Status: {AutonomousCore.system_status}")