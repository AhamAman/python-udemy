# ==========================================
# 1. THE INDEPENDENT COMPONENTS
# ==========================================

class PropulsionSystem:
    def __init__(self, fuel_type: str):
        self.fuel_type = fuel_type
        self.fuel_level = 100.0

    def fire_thrusters(self, burn_time: float):
        """Isolated component logic."""
        fuel_consumed = burn_time * 2.5
        if self.fuel_level >= fuel_consumed:
            self.fuel_level -= fuel_consumed
            print(f"   [Propulsion] Thrusters active. Fuel remaining: {self.fuel_level}%")
            return True
        print("   [Propulsion] ❌ Error: Combustion failure. Fuel exhausted.")
        return False


class ImagingPayload:
    def __init__(self, resolution_megapixels: int):
        self.resolution = resolution_megapixels

    def capture_telemetry(self) -> str:
        """Isolated component logic."""
        print(f"   [Imaging] Exposing camera sensor array ({self.resolution}MP)...")
        return "Image_Data_Matrix_Stream"


# ==========================================
# 2. THE COMPOSITE OBJECT (The Assembly Container)
# ==========================================

class OrbitalSatellite:
    def __init__(self, satellite_name: str):
        self.name = satellite_name
        
        # OBJECT COLLABORATION THROUGH COMPOSITION
        # We instantiate the sub-components directly inside the container object.
        # This satellite 'has-a' propulsion system and 'has-a' camera payload.
        self.propulsion = PropulsionSystem(fuel_type="Hydrazine")
        self.camera = ImagingPayload(resolution_megapixels=150)
        
        print(f"[Satellite Assembly] '{self.name}' successfully integrated.")

    def adjust_orbit_and_scan(self, burn_seconds: float):
        """Coordinates the collective behavior of internal components."""
        print(f"\n>>> '{self.name}' initiating automated tracking command...")
        
        # Delegating tasks down to the specialized internal objects
        thrust_success = self.propulsion.fire_thrusters(burn_time=burn_seconds)
        
        if thrust_success:
            captured_raw_bytes = self.camera.capture_telemetry()
            print(f"[{self.name}] Task Complete. Relaying payload: {captured_raw_bytes}")
        else:
            print(f"[{self.name}] Operation Aborted: Structural adjustment failed.")


# ==========================================
# 3. RUNNING THE SYSTEM
# ==========================================
print("--- Execution Phase ---")

# Create the composite master object
hubble_v2 = OrbitalSatellite("Hubble-V2")

# Run complex operations driven by modular collaboration
hubble_v2.adjust_orbit_and_scan(burn_seconds=4.0)
hubble_v2.adjust_orbit_and_scan(burn_seconds=40.0) # Will exhaust propulsion system