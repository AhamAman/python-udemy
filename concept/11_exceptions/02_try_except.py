def process_user_input(raw_input_value: str):
    """Demonstrates execution steps during successful and failing operations."""
    print(f"\n>>> Entering Gateway Pipeline with Input: '{raw_input_value}'")
    
    try:
        # 1. THE TRY BLOCK
        # This block contains volatile code that *might* throw a runtime exception.
        print("   [Try] Stage 1: Parsing input value...")
        parsed_number = int(raw_input_value)
        
        print("   [Try] Stage 2: Running calculation...")
        # If an exception happens on the line above, Python instantly jumps out.
        # This next line will be completely skipped if input is malformed.
        result = 100 / parsed_number
        
        print(f"   [Try] Stage 3: Operational Success! Result = {result}")

    except ValueError:
        # 2. THE EXCEPT BLOCK
        # This block only executes if a 'ValueError' occurs inside the try block.
        print("   [Except] ❌ Handled ValueError: Input string could not be converted to an integer.")
        result = None

    except ZeroDivisionError:
        # You can stack multiple except blocks to catch different structural failures.
        print("   [Except] ❌ Handled ZeroDivisionError: Cannot divide by a zero denominator value.")
        result = None

    # 3. POST-EXCEPTION EXECUTION FLOW
    # Because the errors were caught and handled, execution does not crash.
    # The program cleanly resumes below the try/except matrix.
    print(f"   [Pipeline Status] Resuming normal execution layout. Output: {result}")


# ==========================================
# SIMULATING EXECUTION PATHS
# ==========================================
print("--- Scenario A: Seamless Execution Path (No Exception) ---")
# Follows Try Stage 1 -> Try Stage 2 -> Try Stage 3 -> Post-Pipeline
process_user_input("4")


print("\n--- Scenario B: Interrupted Execution Path (Exception Occurs) ---")
# Follows Try Stage 1 -> Jumps instantly to ValueError Except -> Post-Pipeline
# Notice that Try Stage 2 and 3 are completely skipped!
process_user_input("malformed_string_data")


print("\n--- Scenario C: Alternative Exception Path ---")
# Follows Try Stage 1 -> Try Stage 2 -> Jumps instantly to ZeroDivisionError Except -> Post-Pipeline
process_user_input("0")

print("\nSystem Test Complete: App process survived all runtime faults.")