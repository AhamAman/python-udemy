# Main execution orchestrator script
import sys

# Simulating importing our telemetry_engine module variables
# from telemetry_engine import process_telemetry_batch

print("--- Scenario A: Clean Structural Propagation Chain ---")

def application_gateway(flag: str):
    print(f"\n>>> Application Gateway opening communication tunnel for flag: {flag}")
    
    try:
        # High-level entry point calls into our external engine module
        process_telemetry_batch(flag)
        print(">>> Gateway: Telemetry stream completely clear.")
        
    except ConnectionResetError as external_error:
        # The exception generated deep inside extract_sensor_voltages() 
        # bubbled up across two functions and an entire module boundary to land here!
        print("\n❌ Central Gateway Intercepted Bubbled Exception!")
        print(f"   Root Exception Class: {type(external_error).__name__}")
        print(f"   Root Exception Message: {external_error}")


# 1. Run a successful execution pass
application_gateway(flag="HEALTHY")

# 2. Run a failing pass to observe stack unwinding mechanics
application_gateway(flag="CORRUPT")