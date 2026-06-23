import time

def database_writer_agent():
    print("[Agent] 🔌 Opening database connection...")
    connection_active = True
    
    try:
        while connection_active:
            # The generator pauses here, waiting for data to write
            data = yield "Ready for next database batch"
            
            print(f"[Agent] 💾 Writing block to database: '{data}'")
            # Simulate database write work
            
    except ConnectionResetError as e:
        # PATTERN 1: INTERNAL RECOVERY
        print(f"\n[Agent] 💥 Crisis detected internally: {e}")
        print("[Agent] 🔄 Attempting recovery: Re-establishing database handshake...")
        
        # The generator handles the error and remains alive by yielding a fallback value
        yield "Handshake restored. System recovered."
        
        print("[Agent] 🔄 Resuming secondary backup logging storage...")
        yield "Ready for backup logging storage"
        
    finally:
        # PATTERN 2: CLEANUP LOGIC
        # This always runs whether the generator finishes naturally, 
        # uncaught exceptions occur, or it gets terminated.
        print("[Agent] 🧹 Cleanup: Rolling back uncommitted transactions...")
        print("[Agent] 🔒 Cleanup: Safely closing database connections.")
        connection_active = False


# ============================================================================
# EXECUTION (The Caller Control Flow)
# ============================================================================

if __name__ == "__main__":
    print("--- 1. Initializing Agent ---")
    agent = database_writer_agent()
    
    # Prime the generator to enter the try block and hit the first yield
    initial_status = next(agent)
    print(f"👉 Caller received status: '{initial_status}'")
    
    print("\n--- 2. Normal Operations ---")
    status = agent.send("Batch #1: User Signups")
    print(f"👉 Caller received status: '{status}'")
    
    print("\n--- 3. Injecting a Recoverable Failure via .throw() ---")
    # The database suddenly drops. We inject a ConnectionResetError into the paused yield.
    recovery_status = agent.throw(ConnectionResetError("Database socket dropped unexpectedly!"))
    print(f"👉 Caller received status after throw: '{recovery_status}'")
    
    print("\n--- 4. Continuing Post-Recovery ---")
    final_status = agent.send("Batch #2: Backup Audit Logs")
    print(f"👉 Caller received status: '{final_status}'")
    
    print("\n--- 5. Triggering Final Cleanup ---")
    # Advancing past the final yield ends the generator naturally, triggering `finally`
    try:
        next(agent)
    except StopIteration:
        print("👉 Agent finished execution pipeline.")

    