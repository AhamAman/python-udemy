# ==========================================
# 1. State Retention Closure Architecture
# ==========================================
def initialize_rate_limiter(max_allowed_calls):
    """Outer factory setting the threshold configuration."""
    call_counter = 0  # Free variable trapped inside the enclosing cell object
    
    def check_rate_limit(request_id):
        nonlocal call_counter  # Allows inner mutation of the enclosing state layer
        call_counter += 1
        
        if call_counter > max_allowed_calls:
            return f"[DENIED] Request {request_id} dropped. Threshold {max_allowed_calls} exceeded."
        return f"[GRANTED] Request {request_id} processed. Total hits: {call_counter}"
        
    return check_rate_limit


# Instantiate an isolated rate-limiting profile
api_gate = initialize_rate_limiter(max_allowed_calls=2)

print("--- 1. Execution Path ---")
print(api_gate("REQ_101"))
print(api_gate("REQ_102"))
print(api_gate("REQ_103")) # Exceeds limit


# ==========================================
# 2. Debugging & Introspecting Closures
# ==========================================
print("\n--- 2. Internal Memory Inspection ---")

# We can peer inside the physical closure blueprint using Python meta-attributes
print(f"Is api_gate a function? {type(api_gate)}")
print(f"Closure cells address:  {api_gate.__closure__}")

# Extracting the living content values inside the cell memory slots
for index, cell in enumerate(api_gate.__closure__):
    print(f"  Cell [{index}] content state: {cell.cell_contents}")