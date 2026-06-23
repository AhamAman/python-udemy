class SmartThermostat:
    def __init__(self, room_name: str, initial_celsius: float):
        self.room_name = room_name
        
        # We assign to self.celsius (the property setter) right away 
        # so our validation logic runs even during object initialization!
        self.celsius = initial_celsius

    # ==========================================
    # 1. GETTER METHOD (The Foundation)
    # ==========================================
    @property
    def celsius(self) -> float:
        """
        The Getter: Intercepts reads (e.g., print(thermostat.celsius)).
        It acts as a shield protecting the internal hidden attribute `_celsius`.
        """
        print(f"[Getter] Fetching temperature for {self.room_name}...")
        return self._celsius

    # ==========================================
    # 2. SETTER METHOD (Validation Pattern)
    # ==========================================
    @celsius.setter
    def celsius(self, new_temp: float):
        """
        The Setter: Intercepts assignments (e.g., thermostat.celsius = 22.5).
        Provides a gatekeeping layer to validate incoming data.
        """
        print(f"[Setter] Attempting to update temperature to {new_temp}°C...")
        
        if not isinstance(new_temp, (int, float)):
            raise TypeError("Temperature must be a numerical value.")
            
        # Hard physical boundary validation
        if new_temp < -50.0 or new_temp > 60.0:
            raise ValueError("Temperature out of safe operating range (-50°C to 60°C).")
            
        self._celsius = float(new_temp)

    # ==========================================
    # 3. COMPUTED ATTRIBUTES (Dynamic Properties)
    # ==========================================
    @property
    def fahrenheit(self) -> float:
        """
        A Computed Attribute: This state does NOT exist as a variable.
        It is derived dynamically from existing state when requested.
        """
        print("[Computed Property] Calculating Fahrenheit on the fly...")
        return (self._celsius * 9/5) + 32

    # ==========================================
    # 4. DELETER METHOD (Cleanup)
    # ==========================================
    @celsius.deleter
    def celsius(self):
        """
        The Deleter: Intercepts resource deletion (e.g., del thermostat.celsius).
        """
        print(f"[Deleter] Resetting {self.room_name} temperature sensor defaults...")
        self._celsius = 0.0


# ==========================================
# RUNNING THE CODE
# ==========================================
print("--- Phase 1: Object Initialization ---")
# Notice that the setter runs immediately during __init__
living_room = SmartThermostat("Living Room", 21.0)

print("\n--- Phase 2: Reading & Writing Properties ---")
# Accessing getter (No parentheses needed!)
print(f"Current State: {living_room.celsius}°C")

# Triggering the setter validation loop
living_room.celsius = 24.5
print(f"Updated State: {living_room.celsius}°C")

print("\n--- Phase 3: Computed Attributes ---")
# Reading a value that isn't stored anywhere explicitly
print(f"Fahrenheit Reading: {living_room.fahrenheit}°F")

print("\n--- Phase 4: Error Handling & Validation ---")
try:
    # This should trip our setter's guardrail validation
    living_room.celsius = 105.0
except ValueError as e:
    print(f"Caught Expected Error: {e}")

print("\n--- Phase 5: Resetting State via Deleter ---")
del living_room.celsius
print(f"Post-Deleter State: {living_room.celsius}°C")