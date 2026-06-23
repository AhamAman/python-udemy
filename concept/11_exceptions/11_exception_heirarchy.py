# ==========================================
# 1. DESIGNING A USER-DEFINED HIERARCHY
# ==========================================

class TelemetrySystemError(Exception):
    """The Root Parent Exception for our entire domain module."""
    pass


class SensorCommunicationError(TelemetrySystemError):
    """A Intermediate Tier Category for hardware link dropouts."""
    pass


class ConnectionTimeoutError(SensorCommunicationError):
    """A Specific Child Leaf representing a precise timing failure boundary."""
    pass


class InvalidChecksumError(SensorCommunicationError):
    """A Specific Child Leaf representing data corruption over the wire."""
    pass


# ==========================================
# 2. RUNNING INDEPENDENT SIMULATION HOOKS
# ==========================================

def read_hardware_payload(status: str):
    print(f"\n[Hardware Array] Simulating state read: {status}")
    if status == "TIMEOUT":
        raise ConnectionTimeoutError("Sensor array failed to respond within 50ms.")
    elif status == "CORRUPT":
        raise InvalidChecksumError("Data frame failed cyclic redundancy check validation.")
    elif status == "CRITICAL_SYSTEM_FAULT":
        raise TelemetrySystemError("Internal hardware matrix circuit configuration compromised.")


# ==========================================
# 3. INTERCEPTING THE HIERARCHY LEVELS
# ==========================================
print("--- Scenario A: Targeted Specific Child Catching ---")

try:
    read_hardware_payload(status="TIMEOUT")
except ConnectionTimeoutError as precise_error:
    # This handler targets ONLY this specific leaf. It leaves other errors alone.
    print(f"   ✅ [Local Recovery] Initiating 3-tier automated packet retry loop: {precise_error}")


print("\n--- Scenario B: Broad Intermediate Parent Catching ---")

for fault_type in ["TIMEOUT", "CORRUPT"]:
    try:
        read_hardware_payload(status=fault_type)
    except SensorCommunicationError as intermediate_error:
        # This single handler captures ConnectionTimeoutError AND InvalidChecksumError
        # because both inherit directly from SensorCommunicationError!
        print(f"   ✅ [Category Recovery] Logged communication fault to diagnostic telemetry: {type(intermediate_error).__name__}")


print("\n--- Scenario C: The Inheritance Trap (Ordering Faults) ---")

try:
    read_hardware_payload(status="CORRUPT")
except TelemetrySystemError as broad_parent_error:
    # ❌ PITFALL: Because TelemetrySystemError sits at the root of our hierarchy,
    # placing this except block at the top will capture ALL subclasses, stealing
    # exceptions from any specific child handlers placed underneath it!
    print(f"   ⚠️ [Broad Parent Interception] Caught failure via root node: {type(broad_parent_error).__name__}")
except InvalidChecksumError:
    print("   This line is dead code. It can never be reached!")