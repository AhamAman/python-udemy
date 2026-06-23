# ==========================================
# Production Structural Pattern Matching
# ==========================================
def route_telemetry_event(event_payload):
    print(f"Incoming Payload to process: {event_payload}")
    
    match event_payload:
        # Pattern 1: Match flat command strings
        case "SYSTEM_HALT":
            return "Action: Immediate hardware power down sequence initiated."
            
        case "SYSTEM_REBOOT":
            return "Action: Cycling socket connections cleanly."
            
        # Pattern 2: Matching a 2-item list/tuple layout (Destructuring)
        # Binds the second element directly to the local variable 'code'
        case ["ERROR", code]:
            return f"Action: Alarm raised. Routing code {code} to diagnostics team."
            
        # Pattern 3: Deeply matching a dict with nested structures & Pattern Guard
        # Matches if type is 'sensor' AND 'reading' is > 100
        case {"type": "sensor", "location": zone, "reading": value} if value > 100:
            return f"Action: CRITICAL! {zone} sensor report over limit at {value}°C. Triggering venting."
            
        # Pattern 4: Matching a dict with nested structures (Normal reading fallback)
        case {"type": "sensor", "location": zone, "reading": value}:
            return f"Action: Logged normal metric for {zone}: {value}°C."
            
        # Pattern 5: Catch-all wildcard fallback (_)
        case _:
            return "Action: Discarded unknown or corrupted package payload configuration."


# ==========================================
# Operational Execution Runs
# ==========================================

# Test 1: Simple text match
print(route_telemetry_event("SYSTEM_HALT"))
print("-" * 50)

# Test 2: List destructuring extraction
print(route_telemetry_event(["ERROR", 503]))
print("-" * 50)

# Test 3: Dictionary pattern matched via condition guard
critical_alert = {"type": "sensor", "location": "Server_Room_B", "reading": 124}
print(route_telemetry_event(critical_alert))
print("-" * 50)

# Test 4: Unrecognized junk hitting fallback wildcard
corrupted_api_data = {"user": "hacker", "payload": [1, 2, 3, 4]}
print(route_telemetry_event(corrupted_api_data))