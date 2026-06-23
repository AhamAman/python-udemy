class MedicalMonitor:
    """
    Models an independent medical monitoring device tracking unique patient data.
    Demonstrates the lifecycle and isolation of instance variables.
    """
    
    def __init__(self, patient_name: str, baseline_heart_rate: int):
        # ==========================================
        # INITIALIZATION PATTERN
        # ==========================================
        # Using 'self.' binds these variables directly to the unique object 
        # instance currently being constructed in memory.
        self.patient = patient_name
        self.heart_rate = baseline_heart_rate
        self.is_critical = False  # Derived state initialized with a default value

    # ==========================================
    # INSTANCE-SPECIFIC BEHAVIOR
    # ==========================================
    def update_vitals(self, current_rate: int):
        """Modifies the unique instance state based on real-time data."""
        self.heart_rate = current_rate
        
        # Behavior diverges dynamically based on this specific object's data
        if self.heart_rate > 100 or self.heart_rate < 50:
            self.is_critical = True
        else:
            self.is_critical = False
            
    def display_status(self):
        """Displays status pulling entirely from self-contained instance state."""
        alert_status = "⚠️ CRITICAL ALERT" if self.is_critical else "✅ Stable"
        print(f"Patient: {self.patient:<10} | Vitals: {self.heart_rate} BPM | Status: {alert_status}")


# ==========================================
# RUNNING THE INDEPENDENT STATE EXPERIMENT
# ==========================================
print("--- Phase 1: Allocating Independent Objects ---")

# We use one blueprint to instantiate two completely isolated patient profiles
monitor_patient_a = MedicalMonitor(patient_name="Alice", baseline_heart_rate=72)
monitor_patient_b = MedicalMonitor(patient_name="Bob", baseline_heart_rate=68)

# Introspecting internal data stores to prove isolation
print(f"Patient A Local Memory Space (__dict__): {monitor_patient_a.__dict__}")
print(f"Patient B Local Memory Space (__dict__): {monitor_patient_b.__dict__}")


print("\n--- Phase 2: Demonstrating State Isolation ---")

# We mutate Patient B's vitals. Patient A's memory block remains completely untouched.
monitor_patient_b.update_vitals(current_rate=125)

print("Displaying current system snapshot:")
monitor_patient_a.display_status() # Pulls from Patient A's memory
monitor_patient_b.display_status() # Pulls from Patient B's memory


print("\n--- Phase 3: Dynamic Runtime Attribute Injection ---")

# Because Python instance variables live inside an underlying dictionary, 
# you can technically inject instance variables on the fly outside of __init__
monitor_patient_a.room_number = 402

print(f"Patient A Room Number: {monitor_patient_a.room_number}")
print(f"Patient A Updated Storage: {monitor_patient_a.__dict__}")

# Critical Check: Trying to access this on Patient B throws an error because its dict doesn't contain the key
try:
    print(monitor_patient_b.room_number)
except AttributeError as e:
    print(f"❌ Patient B Check Blocked: {e}")