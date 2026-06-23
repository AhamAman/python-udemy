import inspect

# ==========================================
# 1. Defining the State Tracking Generator
# ==========================================
def hardware_telemetry_generator():
    """A clear state machine that preserves internal iteration tracking states."""
    print("    [GEN-CORE] Ignition sequence started.")
    
    # Internal state variables that will be frozen on the heap
    running_total_metric = 0
    
    # Active Loop Structure Tracking
    for loop_index in range(1, 4):
        running_total_metric += loop_index * 10
        
        print(f"    [GEN-CORE] Pausing at yield. Loop Index: {loop_index} | Total: {running_total_metric}")
        yield f"FRAME_DATA::{running_total_metric}"
        
        # When un-freezing, Python restores loop_index and running_total_metric perfectly
        print(f"    [GEN-CORE] Resuming frame space. Loop Index {loop_index} is intact.")
        
    print("    [GEN-CORE] Code path exhausted cleanly.")


# ==========================================
# 2. Tracking State Transitions
# ==========================================
print("--- Phase 1: Tracking Structural State Transitions ---")

# Step A: Instantiate the generator
telemetry_stream = hardware_telemetry_generator()
print(f"State immediately after instantiation: {inspect.getgeneratorstate(telemetry_stream)}")

# Step B: Wake the engine up and advance to the first yield point
print("\n--- Invoking next() #1 ---")
data_frame_1 = next(telemetry_stream)
print(f"Consumer Intercepted: {data_frame_1}")
print(f"State while suspended at yield line:  {inspect.getgeneratorstate(telemetry_stream)}")


# ==========================================
# 3. Proving Variable Preservation Inside Loops
# ==========================================
print("\n--- Phase 2: Verifying Loop and Variable Memory Retention ---")

# Step C: Advance to the second yield point
print("\n--- Invoking next() #2 ---")
data_frame_2 = next(telemetry_stream)
print(f"Consumer Intercepted: {data_frame_2}")

# Step D: Consume the remaining elements until the stream is exhausted
print("\n--- Finalizing Stream Consumption ---")
for frame in telemetry_stream:
    print(f"Loop Consumer Auto-Intercepted: {frame}")

# Verify the final terminal state
print(f"\nState after full execution cleanup:   {inspect.getgeneratorstate(telemetry_stream)}")