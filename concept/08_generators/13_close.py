import io

def live_sensor_stream():
    # Simulate allocating a heavy system resource (like a file stream or socket)
    print("[Sensor] 🔌 Allocating system resource: Opening Sensor Stream...")
    mock_sensor_file = io.StringIO("DataLine1\nDataLine2\nDataLine3\nDataLine4\n")
    
    try:
        while True:
            line = mock_sensor_file.readline()
            if not line:
                break
            # Yield out data and pause
            yield line.strip()
            
    except GeneratorExit:
        # This block catches the close signal explicitly
        print("[Sensor] 🛑 Received close() signal via GeneratorExit.")
        # You can do early cleanup here if needed
        raise # Good practice to let it propagate, though Python handles it automatically
        
    finally:
        # This is guaranteed to run, whether it finishes naturally or gets closed
        print("[Sensor] 🧹 Finalization: Flushing buffers...")
        mock_sensor_file.close()
        print("[Sensor] 🔒 Resource Safely Closed.")


# ============================================================================
# EXECUTION (The Caller Control Flow)
# ============================================================================

if __name__ == "__main__":
    print("--- 1. Initializing and Starting Stream ---")
    stream = live_sensor_stream()
    
    # Read a few lines of data
    print(f"👉 Caller pulled: {next(stream)}")
    print(f"👉 Caller pulled: {next(stream)}")
    
    print("\n--- 2. Caller decides to break early and close the stream ---")
    # This triggers the GeneratorExit exception inside the generator's current yield
    stream.close()
    
    print("\n--- 3. Post-Close Behavior ---")
    # Once closed, calling next() on it safely raises StopIteration
    try:
        next(stream)
    except StopIteration:
        print("👉 Stream is dead. Safe to proceed.")

