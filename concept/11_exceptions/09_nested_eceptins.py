import json

# Custom exception representing a localized, recoverable data issue
class CorruptTelemetryError(ValueError): pass


# ==========================================
# 1. NESTING INSIDE FUNCTIONS & LOOPS
# ==========================================

def parse_raw_packet(raw_string: str) -> dict:
    """Inner isolated helper function."""
    try:
        # Volatile step: Vulnerable to JSON structural faults
        return json.loads(raw_string)
    except json.JSONDecodeError as err:
        # Intercepting standard JSON errors and converting them into a domain-specific exception
        raise CorruptTelemetryError(f"Malformed JSON syntax: {err}")


def execute_master_ingestion_pipeline(stream_packets: list):
    """Outer manager function handling a sequential data loop."""
    print(f">>> Beginning ingestion processing for {len(stream_packets)} data packets...")
    
    # Outer Try Block: Shields the entire pipeline from catastrophic system failure
    try:
        processed_records = []
        
        for index, packet in enumerate(stream_packets, start=1):
            print(f"\n   [Loop Step {index}] Processing packet data...")
            
            # INNER TRY BLOCK (Inside a Loop):
            # Isolates individual packet errors so a single corrupted data frame
            # doesn't crash the entire multi-packet batch.
            try:
                data_dict = parse_raw_packet(packet)
                
                # Check for an explicit system shutdown signal
                if data_dict.get("command") == "SHUTDOWN":
                    raise SystemExit("Immediate emergency operator halt requested.")
                    
                metric_value = data_dict["reading"]
                processed_records.append(metric_value * 1.5)
                print(f"      [Inner Success] Appended metric calculation.")
                
            except CorruptTelemetryError as local_err:
                # Recovering locally from a predictable, non-fatal issue
                print(f"      [Inner Handler] Recovered from bad packet: {local_err}")
                print("      [Inner Handler] Skipping packet and moving to the next item...")
                continue # The loop survives and advances!
                
        print(f"\n[Pipeline Complete] Batch executed. Records compiled: {processed_records}")

    # OUTER EXCEPT BLOCKS:
    # Catches major structural failures that the inner block chose not to handle,
    # or failures that explicitly bubbled out.
    except KeyError as mapping_err:
        print(f"\n❌ [Outer Handler] Pipeline Terminated: Missing required 'reading' key fields: {mapping_err}")
    except SystemExit as exit_signal:
        print(f"\n❌ [Outer Handler] Pipeline Gracefully Aborted: {exit_signal}")


# ==========================================
# 2. RUNNING THE NESTED LOOPS
# ==========================================
print("--- Test Run 1: Local Inner Recovery ---")
# Packet 2 is completely broken JSON, but the inner loop intercepts it, skips it, and processes Packet 3.
mixed_batch = ['{"reading": 10}', '{broken_json_string}', '{"reading": 20}']
execute_master_ingestion_pipeline(mixed_batch)


print("\n--- Test Run 2: Outer Exception Bubbling ---")
# Packet 1 matches JSON syntax, but lacks the 'reading' key. 
# The inner block doesn't catch KeyError, so it bubbles up and shuts down the entire outer pipeline.
unmapped_batch = ['{"status": "offline"}', '{"reading": 50}']
execute_master_ingestion_pipeline(unmapped_batch)


print("\n--- Test Run 3: Intentional System Propagation ---")
# SystemExit bubbles straight out of the inner block to be cleanly managed by the outer handler.
emergency_batch = ['{"reading": 12}', '{"command": "SHUTDOWN"}']
execute_master_ingestion_pipeline(emergency_batch)

