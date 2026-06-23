class CoreNuclearReactor:
    def __init__(self, location: str, initial_temp: float):
        # 1. PUBLIC ATTRIBUTE
        # Accessible from anywhere, inside or outside the class.
        self.location = location

        # 2. PROTECTED ATTRIBUTE (Single Underscore Convention)
        # Signaled as internal/semi-private. Python does NOT enforce this at runtime,
        # but developers and linters treat it as a warning: "Do not touch outside this class tree."
        self._coolant_level = 100.0

        # 3. PRIVATE ATTRIBUTE (Double Underscore Trigger)
        # Triggers Python's internal Name Mangling engine to prevent accidental overrides.
        self.__core_temperature = initial_temp

    # Public method acting as a controlled interface to private data
    def check_safety_status(self) -> str:
        """Controlled reading interface (Getter logic)."""
        # Inside the class, we can read __core_temperature seamlessly
        if self.__core_temperature > 1500.0:
            return "🚨 CRITICAL OVERHEAT ALERT"
        return "✅ Normal Operations"

    def inject_coolant(self, amount: float):
        """Controlled mutation interface (Setter logic)."""
        print(f"\n[System Control] Injecting {amount}L of coolant...")
        self._coolant_level += amount
        # Safe internal state mutation
        self.__core_temperature -= amount * 2.5


# ==========================================
# RUNNING THE ENCAPSULATION EXPERIMENT
# ==========================================
print("--- Phase 1: Accessing Public and Protected Fields ---")
reactor = CoreNuclearReactor(location="Sector 7-G", initial_temp=1200.0)

# Public access works anywhere
print(f"Reactor Location: {reactor.location}")

# Protected access: Python allows this to execute because it's a convention, 
# but doing this from an external script violates clean design rules.
print(f"Current Coolant Level (Direct Read): {reactor._coolant_level}%")


print("\n--- Phase 2: The Private Field & Name Mangling Trap ---")

try:
    # Attempting to read or write a double-underscore attribute directly will fail
    print(reactor.__core_temperature)
except AttributeError as e:
    print(f"❌ Direct Access Blocked: {e}")


# Introspection: Let's view the actual dictionary keys stored in memory for this object
print(f"\nLive Object Storage Keys: {list(reactor.__dict__.keys())}")

# Notice how '__core_temperature' was mutated into '_CoreNuclearReactor__core_temperature'!
# This is Name Mangling. You can technically bypass Python's private shield by calling the mangled name:
mangled_read = reactor._CoreNuclearReactor__core_temperature
print(f"Bypassing via Mangled Name: {mangled_read}°C")


print("\n--- Phase 3: Interface Isolation ---")
# The correct way to interact with encapsulated state is through explicit methods
print(f"Initial Status Check: {reactor.check_safety_status()}")
reactor.inject_coolant(150.0)
print(f"Post-Coolant Status Check: {reactor.check_safety_status()}")