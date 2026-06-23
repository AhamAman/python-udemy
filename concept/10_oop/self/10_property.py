class PowerGridNode:
    def __init__(self, node_id: str, initial_voltage: float):
        self.node_id = node_id
        
        # Calling self.voltage runs our @voltage.setter validation 
        # immediately during object instantiation!
        self.voltage = initial_voltage

    # ==========================================
    # 1. THE GETTER METHOD
    # ==========================================
    @property
    def voltage(self) -> float:
        """
        The Getter: Intercepts reads (e.g., current = node.voltage).
        It acts as a gateway to our protected internal attribute `_voltage`.
        """
        print(f"   [Property Getter] Reading voltage level for node '{self.node_id}'...")
        return self._voltage

    # ==========================================
    # 2. THE SETTER METHOD (Validation Pattern)
    # ==========================================
    @voltage.setter
    def voltage(self, new_value: float):
        """
        The Setter: Intercepts modifications (e.g., node.voltage = 400).
        Enforces defensive safety constraints before writing to memory.
        """
        print(f"   [Property Setter] Intercepted modification request to: {new_value}V")
        
        if not isinstance(new_value, (int, float)):
            raise TypeError("Voltage assignment failed: Value must be numerical.")
            
        # Hard system boundary validation
        if new_value < 0 or new_value > 5000:
            raise ValueError("Voltage assignment failed: Exceeds safe network limits (0V - 5000V).")
            
        self._voltage = float(new_value)

    # ==========================================
    # 3. COMPUTED ATTRIBUTES (Dynamic Properties)
    # ==========================================
    @property
    def kilo_volts(self) -> float:
        """
        A Computed Attribute: This state does NOT exist as a saved variable.
        It calculates a value dynamically from existing state on demand.
        """
        print("   [Computed Property] Calculating Kilovolts on the fly...")
        return self._voltage / 1000.0

    # ==========================================
    # 4. THE DELETER METHOD
    # ==========================================
    @voltage.deleter
    def voltage(self):
        """The Deleter: Intercepts field erasure (e.g., del node.voltage)."""
        print(f"   [Property Deleter] Safety reset initiated. Purging voltage state...")
        self._voltage = 0.0


# ==========================================
# RUNNING THE PROPERTY PIPELINE
# ==========================================
print("--- Phase 1: Instantiation & Inherent Validation ---")
# The setter checks our value before the object even fully finishes loading
node_alpha = PowerGridNode(node_id="Transformer-04", initial_voltage=240.0)

print("\n--- Phase 2: Intercepting Reads & Writes ---")
# Reading the property like a variable (Notice: No trailing parentheses needed!)
print(f"Current Reading: {node_alpha.voltage}V")

# Triggering the validation layer via assignment syntax
node_alpha.voltage = 480.0
print(f"New Reading: {node_alpha.voltage}V")

print("\n--- Phase 3: Computed Attributes ---")
# Fetching a state that isn't explicitly tracked by an internal variable
print(f"Kilovolts Reading: {node_alpha.kilo_volts} kV")

print("\n--- Phase 4: Defensive Guardrail Failures ---")
try:
    # This should be immediately stopped by our setter validation loop
    node_alpha.voltage = 99999.0
except ValueError as e:
    print(f"❌ Guardrail Tripped Safely: {e}")

print("\n--- Phase 5: Resource Cleanup via Deleter ---")
del node_alpha.voltage
print(f"Post-Deleter Fallback State: {node_alpha.voltage}V")