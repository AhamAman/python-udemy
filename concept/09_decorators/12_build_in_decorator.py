class TemperatureSensor:
    # A class variable shared across all instances
    _global_unit = "Celsius"

    def __init__(self, location: str, celsius_value: float):
        self.location = location
        # Internal private attribute (prefixed with underscores)
        self._celsius = celsius_value

    # ==========================================
    # 1. PROPERTY, SETTER, AND DELETER
    # ==========================================
    
    @property
    def fahrenheit(self) -> float:
        """
        Acts as a Getter. Turns a method call into an attribute lookup.
        Internal Behavior: Invokes the descriptor's __get__ method.
        """
        print("[Property Getter] Calculating Fahrenheit dynamically...")
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        """
        Acts as a Setter. Intercepts assignment (e.g., obj.fahrenheit = 32).
        Internal Behavior: Invokes the descriptor's __set__ method.
        """
        print(f"[Property Setter] Intercepted new value: {value}°F. Converting to Celsius...")
        if value < -459.67: # Absolute zero validation
            raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = (value - 32) * 5/9

    @fahrenheit.deleter
    def fahrenheit(self):
        """
        Acts as a Deleter. Intercepts deletion (e.g., del obj.fahrenheit).
        Internal Behavior: Invokes the descriptor's __delete__ method.
        """
        print("[Property Deleter] Resetting internal temperature value...")
        self._celsius = 0.0


    # ==========================================
    # 2. CLASSMETHOD AND STATICMETHOD
    # ==========================================

    @classmethod
    def change_global_unit(cls, new_unit: str):
        """
        Binds the method to the Class itself, not the instance.
        Internal Behavior: Implicitly passes the class object as 'cls'.
        """
        print(f"[Class Method] Modifying global configuration for class: {cls.__name__}")
        cls._global_unit = new_unit

    @staticmethod
    def is_safe_temperature(celsius: float) -> bool:
        """
        Completely unbinds the function from both class and instance.
        Internal Behavior: Behaves exactly like a standard function isolated inside a namespace.
        """
        print(f"[Static Method] Independent utility checking if {celsius}°C is structurally safe...")
        return -50.0 <= celsius <= 100.0


# ==========================================
# 3. RUNNING THE CODE & OBSERVING BEHAVIOR
# ==========================================
print("--- Phase 1: Object Instantiation ---")
sensor = TemperatureSensor(location="Server Room A", celsius_value=25.0)

print("\n--- Phase 2: Property Mechanics ---")
# 1. Accessing getter like an attribute (Notice: No parentheses!)
print(f"Current Temp: {sensor.fahrenheit}°F")

# 2. Triggering setter validation and modification
sensor.fahrenheit = 95.0
print(f"Updated Internal Celsius State: {sensor._celsius:.1f}°C")

# 3. Triggering deleter
del sensor.fahrenheit
print(f"Celsius State After Deletion: {sensor._celsius}°C")

print("\n--- Phase 3: Class vs Static Methods ---")
# Calling classmethod alters global class state
TemperatureSensor.change_global_unit("Fahrenheit")
print(f"Updated global unit: {sensor._global_unit}")

# Calling staticmethod operates purely on inputs provided
is_safe = TemperatureSensor.is_safe_temperature(150.0)
print(f"Is 150°C safe? {is_safe}")