import sys

class ManagedNetworkConnection:
    """A custom context manager simulating an isolated network channel wrapper."""
    
    def __init__(self, target_host: str):
        self.host = target_host
        self.is_connected = False

    # ==========================================
    # 1. SETUP MECHANICS
    # ==========================================
    def __enter__(self):
        """Triggered automatically when entering the 'with' scope."""
        print(f"\n[__enter__] Allocating network socket channel to host: '{self.host}'")
        self.is_connected = True
        
        # The value returned here is what gets assigned to the 'as' variable name
        return self

    # ==========================================
    # 2. CLEANUP & EXCEPTION MECHANICS
    # ==========================================
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Triggered automatically when exiting the 'with' scope.
        Guaranteed to execute, even if the code block crashes.
        
        Parameters passed by Python if an exception occurred:
            exc_type: The class of the exception (e.g., ValueError)
            exc_val:  The exception instance object (e.g., ValueError("Message"))
            exc_tb:   The traceback object tracking execution frames
        """
        print("[__exit__] 🔒 Closing socket connection descriptors. Releasing hardware port.")
        self.is_connected = False

        # Check if we are exiting due to an internal error or normal completion
        if exc_type is not None:
            print(f"   [__exit__] ⚠️ Detected active crash bubble inside scope: {exc_type.__name__}")
            
            if issubclass(exc_type, ConnectionResetError):
                print("   [__exit__] Handled known network drop locally. Suppressing exception.")
                # CRITICAL: Returning True signals to Python that the exception has been 
                # completely handled and should be swallowed. Execution continues below 'with'.
                return True
        
        print("   [__exit__] No suppressed errors. Passing context out.")
        # Returning False (or None) tells Python to let the exception bubble up the call stack
        return False

    def transmit_data(self, payload: str):
        """A sample instance method vulnerable to real-world infrastructure drops."""
        if not self.is_connected:
            raise RuntimeError("Operation Denied: Socket is offline.")
        print(f"   [Transmission] Forwarding packet: '{payload}'")


# ==========================================
# EXECUTING CONTEXT CONTROL LOOPS
# ==========================================
print("--- Run 1: Flawless Execution Flow (Standard Path) ---")

# Executes: __enter__ -> Code Block -> __exit__(None, None, None)
with ManagedNetworkConnection(target_host="api.production.internal") as connection:
    connection.transmit_data("PACKET_01_HEALTHY")
    print("   [Block] Command step complete.")

print("Status Post-With: Channel active? ->", connection.is_connected)


print("\n--- Run 2: Intercepted Exception (Swallowed Error Path) ---")

# Executes: __enter__ -> Code Block (Crashes) -> __exit__(ConnectionResetError...)
with ManagedNetworkConnection(target_host="api.unstable.node") as connection:
    connection.transmit_data("PACKET_02_VOLATILE")
    # Simulate a network disconnection event
    raise ConnectionResetError("Remote server rejected handshake packet down the wire.")
    print("This line will never be reached.")

print("\nStatus Post-With: Script survived the crash because __exit__ returned True.")
print("Channel active? ->", connection.is_connected)


print("\n--- Run 3: Unhandled Exception (Bubbling Path) ---")

try:
    with ManagedNetworkConnection(target_host="api.strict.node") as connection:
        connection.transmit_data("PACKET_03_MALFORMED")
        # Triggering an unexpected programming bug
        raise ValueError("Developer coding calculation bug.")
        
except ValueError as bubbled_error:
    print(f"\n❌ Catch Engine: Intercepted unhandled error that bubbled past __exit__: {bubbled_error}")
    print("Status Post-With: Channel active? ->", connection.is_connected)