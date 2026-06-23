# ==========================================
# 1. Defining a Controlled Stream Generator
# ==========================================
def hardware_sensor_stream():
    """Simulates a telemetry feed with exactly three data frames."""
    print("  [SENSOR] Running ignition sequence...")
    yield "Metric_Alpha"
    
    print("  [SENSOR] Tracking subsequent metric...")
    yield "Metric_Beta"
    
    print("  [SENSOR] Finalizing stream records...")
    yield "Metric_Gamma"
    
    print("  [SENSOR] Stream path complete. Exiting function frame.")
    # Function drops off the bottom here, implicitly raising StopIteration


# ==========================================
# 2. Manual Ingestion Tracking & Catching StopIteration
# ==========================================
print("--- Scenario A: Manual next() Trace and Error Gate ---")

sensor_engine = hardware_sensor_stream()

print("\nExecution Step 1:")
print(f"Consumer Captured: {next(sensor_engine)}")

print("\nExecution Step 2:")
print(f"Consumer Captured: {next(sensor_engine)}")

print("\nExecution Step 3:")
print(f"Consumer Captured: {next(sensor_engine)}")

print("\nExecution Step 4 (Stream is empty, expecting StopIteration):")
try:
    # This call will hit the bottom of the function code path
    next(sensor_engine)
except StopIteration as signal:
    print(f"Caught expected Exception -> StopIteration raised successfully.")


# ==========================================
# 3. Clean Iteration via For Loops
# ==========================================
print("\n--- Scenario B: The for Loop Integration Pattern ---")

# Instantiate a fresh, un-exhausted stream instance
fresh_sensor_engine = hardware_sensor_stream()

# The for loop acts as a structural wrapper, calling next() 
# and catching the StopIteration exception automatically.
for metric in fresh_sensor_engine:
    print(f"Loop Consumer Intercepted: {metric}")

print("\nPipeline terminated cleanly without raising an uncaught exception.")

