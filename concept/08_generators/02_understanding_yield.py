# ==========================================
# 1. Advanced Architecture Definition
# ==========================================
def smart_network_router_generator(routing_rules):
    """A complex state engine demonstrating yield across loops and conditionals."""
    print("  [ROUTER-GEN] Ingestion layer initialized.")
    processed_count = 0  # Persistent internal local state variable
    
    # Outer Loop Track
    for rule in routing_rules:
        processed_count += 1
        
        # Conditional Branch Block
        if rule["action"] == "BYPASS":
            print(f"  [ROUTER-GEN] Rule {processed_count}: Processing BYPASS line...")
            yield f"ACTION::BYPASS for target {rule['target']}"
            # When resumed, the generator wakes up exactly here, inside this 'if' block
            print(f"  [ROUTER-GEN] Handshake confirmed for bypass: {rule['target']}")
            
        elif rule["action"] == "INSPECT":
            print(f"  [ROUTER-GEN] Rule {processed_count}: Entering deep INSPECT loops...")
            
            # Nested Loop Structure Block
            for vulnerability_scan_id in ["CVE-01", "CVE-02"]:
                yield f"ACTION::INSPECT packet {rule['target']} query: {vulnerability_scan_id}"
                # Every single step of this nested loop preserves processed_count and current IDs
                
        else:
            yield f"ACTION::DROP unauthorized rule for target {rule['target']}"
            
    print("  [ROUTER-GEN] All pipeline rules exhausted cleanly.")


# ==========================================
# 2. Execution Tracing
# ==========================================
print("--- 1. Initiating Execution and Tracking State ---")

network_payload = [
    {"action": "BYPASS",  "target": "Server_Alpha"},
    {"action": "INSPECT", "target": "Gateway_Beta"}
]

# Instantiate the stream
stream_engine = smart_network_router_generator(network_payload)

# Step A: Run to the first yield point (Inside the if condition)
print("\n--- Triggering next() #1 ---")
print(f"Consumer Received -> {next(stream_engine)}")

# Step B: Resume and watch it pick up inside the if block, then transition to the nested loop
print("\n--- Triggering next() #2 ---")
print(f"Consumer Received -> {next(stream_engine)}")

# Step C: Step through the nested loop
print("\n--- Triggering next() #3 ---")
print(f"Consumer Received -> {next(stream_engine)}")


# ==========================================
# 3. Stream Exhaustion Verification
# ==========================================
print("\n--- 2. Exhaustion Verification Phase ---")

# Fully exhaust the remaining elements in the generator loop safely using a for loop
for analytical_frame in stream_engine:
    print(f"Loop Consumer Intercepted -> {analytical_frame}")

print("\nAttempting to call next() on the dead stream:")
try:
    next(stream_engine)
except StopIteration:
    print("Caught expected StopIteration: The generator is exhausted and its frame is dead.")