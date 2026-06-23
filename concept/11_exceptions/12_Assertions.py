def calculate_system_throughput(buffer_units: int, processing_time: float) -> float:
    """Computes operational processing speeds under strict internal constraints."""
    
    # ==========================================
    # 1. ENFORCING INTERNAL DEVELOPER SANITY CHECKS
    # ==========================================
    # Syntax: assert <condition>, <optional_diagnostic_message_string>
    # These verify structural assumptions that should be physically impossible to break 
    # unless a developer introduced a bug into the calling codebase.
    assert buffer_units >= 0, f"Bug Detected: Buffer units cannot be a negative vector layout. Got: {buffer_units}"
    assert processing_time > 0, f"Bug Detected: Time vector must be positive and non-zero. Got: {processing_time}"
    
    # Core mathematical business logic execution
    raw_throughput = buffer_units / processing_time
    
    # Post-condition internal validation: Ensure our calculation didn't yield an unphysical state
    assert raw_throughput >= 0, "Bug Detected: Calculated throughput matrix yielded an impossible negative value."
    
    return raw_throughput


# ==========================================
# EXECUTING RUNTIME EVALUATIONS
# ==========================================
print("--- Phase 1: Valid Execution Loop ---")
output = calculate_system_throughput(buffer_units=500, processing_time=2.5)
print(f"System Operational Throughput: {output} units/sec")


print("\n--- Phase 2: Tripping an Internal Assertion Gate ---")
try:
    # A developer mistakenly passes a negative processing time parameter down the line
    calculate_system_throughput(buffer_units=500, processing_time=-0.5)
except AssertionError as assertion_fault:
    print(f"❌ Structural Crash Intercepted: {type(assertion_fault).__name__}")
    print(f"   Diagnostic Message: {assertion_fault}")