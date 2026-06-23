import json

# Custom system-level exception built specifically for this application layer
class DeviceTelemetryFormatError(ValueError):
    """Custom exception inheriting from the built-in ValueError parent class."""
    pass


def parse_device_transmission(raw_payload: str):
    """Processes incoming data streams under explicit exception-matching guardrails."""
    print(f"\n>>> Parsing Network Transmission Payload...")
    
    try:
        # Volatile parsing sequence
        if not raw_payload:
            raise DeviceTelemetryFormatError("Payload cannot be completely empty.")
            
        parsed_json = json.loads(raw_payload)
        metric_value = parsed_json["reading"]
        calculated_factor = 100 / metric_value
        print(f"   [Success] Value computed cleanly: {calculated_factor}")

    # ==========================================
    # CATCHING SPECIFIC EXCEPTIONS (CORRECT ORDER)
    # ==========================================
    
    # 1. Catch our highly specialized child exception first
    except DeviceTelemetryFormatError as custom_err:
        print(f"   [Handler: Custom Error] 🚨 Telemetry Malformed: {custom_err}")
        
    # 2. Catch the built-in parent class next.
    # If ValueError sat above DeviceTelemetryFormatError, it would steal its exceptions!
    except ValueError as standard_err:
        print(f"   [Handler: Standard ValueError] JSON decoding step completely failed: {standard_err}")

    # 3. Catching multiple specific exceptions simultaneously inside a single tuple
    except (KeyError, ZeroDivisionError) as mapping_or_math_err:
        print(f"   [Handler: Group Tuple] Structural or Math Failure: Caught {type(mapping_or_math_err).__name__} -> {mapping_or_math_err}")

    # ==========================================
    # THE BROAD EXCEPT TRAP (The Safety Net)
    # ==========================================
    except Exception as broad_err:
        # This is a broad catch. It should ONLY exist at the absolute bottom of your stack 
        # as a fallback handler for unexpected framework drops (e.g., OutOfMemory or KeyboardInterrupt errors).
        print(f"   [Handler: Broad Exception Fallback] Intercepted unpredicted crash path: {broad_err}")


# ==========================================
# EXECUTING EXCEPTION MATCHING WORKFLOWS
# ==========================================
print("--- Test Suite Execution ---")

# Trigger 1: Fires DeviceTelemetryFormatError (Handled by Exception Block 1)
parse_device_transmission("")

# Trigger 2: Fires a standard ValueError via json.loads (Handled by Exception Block 2)
parse_device_transmission("{invalid_json_brackets}")

# Trigger 3: Fires a KeyError (Handled by Exception Block 3 Tuple)
parse_device_transmission('{"status": "active"}') # Missing the 'reading' key

# Trigger 4: Fires a ZeroDivisionError (Handled by Exception Block 3 Tuple)
parse_device_transmission('{"reading": 0}')