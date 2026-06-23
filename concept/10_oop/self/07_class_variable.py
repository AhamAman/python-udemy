class OrbitalSatellite:
    # ==========================================
    # 1. CLASS VARIABLES (Shared State)
    # ==========================================
    # These live on the Class namespace. All instances share these.
    global_gravitational_constant = 9.80665
    active_satellite_count = 0
    active_frequencies = [] # A mutable class variable (Danger Zone!)

    def __init__(self, satellite_id: str):
        # ==========================================
        # 2. INSTANCE VARIABLES (Unique State)
        # ==========================================
        # These live strictly inside the individual object's __dict__
        self.satellite_id = satellite_id
        
        # Incrementing the shared class variable safely by targeting the Class itself
        OrbitalSatellite.active_satellite_count += 1


# ==========================================
# RUNNING THE MECHANICS EXPERIMENT
# ==========================================
print("--- Phase 1: Shared Reading via Resolution Order ---")

sat_alpha = OrbitalSatellite("Alpha-1")
sat_beta = OrbitalSatellite("Beta-2")

# 1. Accessing shared data via the Class directly
print(f"Count via Class: {OrbitalSatellite.active_satellite_count}")

# 2. Accessing shared data via the Instances
# Python looks into sat_alpha.__dict__ (fails), then climbs to OrbitalSatellite.__dict__ (succeeds)
print(f"Count via Alpha: {sat_alpha.active_satellite_count}")
print(f"Count via Beta:  {sat_beta.active_satellite_count}")


print("\n--- Phase 2: Modifying Class Variables (The Correct Way) ---")

# To change a class variable for EVERY instance simultaneously, mutate it on the Class object.
OrbitalSatellite.global_gravitational_constant = 9.780
print(f"Updated Alpha Constant: {sat_alpha.global_gravitational_constant}")
print(f"Updated Beta Constant:  {sat_beta.global_gravitational_constant}")


print("\n--- Phase 3: Pitfall 1 - Shadowing via Instance Assignment ---")

# What happens if we try to modify the class variable through an instance pointer?
sat_alpha.global_gravitational_constant = 1.622 # Intending to change it for alpha
print(f"Alpha Constant: {sat_alpha.global_gravitational_constant} (Changed)")
print(f"Beta Constant:  {sat_beta.global_gravitational_constant} (Unchanged!)")
print(f"Class Constant: {OrbitalSatellite.global_gravitational_constant} (Unchanged!)")

# Why? Because assignment (=) on an instance forces Python to create a NEW 
# instance variable inside sat_alpha.__dict__, shadowing the class variable.
print(f"Alpha local storage keys: {list(sat_alpha.__dict__.keys())}")


print("\n--- Phase 4: Pitfall 2 - The Mutable Shared List Trap ---")

# If an instance alters a MUTABLE class variable (like a list) without an explicit assignment (=),
# it leaks into every single object across your system.
sat_alpha.active_frequencies.append("1420 MHz")

print(f"Alpha Frequencies: {sat_alpha.active_frequencies}")
print(f"Beta Frequencies:  {sat_beta.active_frequencies} (Accidentally mutated!)")