import io

def simulate_data_pipeline(data_payload: str, process_successfully: bool):
    print(f"\n>>> Opening Pipeline Session [Payload Length: {len(data_payload)}]...")
    
    # Simulating a system resource allocation block (e.g., file descriptor or socket)
    mock_io_stream = io.StringIO(data_payload)
    
    try:
        print("   [Try] Reading stream data blocks into volatile memory...")
        stream_contents = mock_io_stream.read()
        
        if not process_successfully:
            # Triggering a deliberate runtime crash
            calculated_fault = 100 / 0
            
    except ZeroDivisionError as error:
        print(f"   [Except] Intercepted math error layer: {error}")
        # Even if we return straight out of the except block, finally WILL still execute!
        return "Failure State Handled"

    else:
        # ==========================================
        # THE POWER OF THE else BLOCK
        # ==========================================
        # This code runs ONLY if the try block succeeds perfectly.
        # Placing logic here rather than inside the try block ensures that if
        # an unexpected ValueError occurs inside 'process_metrics', it won't 
        # be accidentally swallowed by our 'except ZeroDivisionError' block.
        print("   [Else] Success path unlocked. Executing deep downstream analytics...")
        processed_output = stream_contents.upper()
        print(f"   [Else] Metric Result: {processed_output}")
        return f"Success Output: {processed_output}"

    finally:
        # ==========================================
        # THE GUARANTEE OF THE finally BLOCK
        # ==========================================
        # This block executes no matter what path the function took.
        # Whether the code succeeded, threw an exception, or hit an early return statement,
        # the finally block acts as a clean closer to free up system resources.
        print("   [Finally] 🔒 Closing IO stream blocks. Memory safely deallocated.")
        mock_io_stream.close()


# ==========================================
# EXECUTING RUNTIME FLOW SCENARIOS
# ==========================================
print("--- Run 1: Evaluating the Success Path ---")
# Executes: try -> else -> finally
run_one = simulate_data_pipeline(data_payload="sensor_matrix_data", process_successfully=True)
print(f"Function Returned: {run_one}")


print("\n--- Run 2: Evaluating the Exception Path ---")
# Executes: try -> except -> finally
run_two = simulate_data_pipeline(data_payload="corrupt_payload", process_successfully=False)
print(f"Function Returned: {run_two}")