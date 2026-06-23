# ==========================================
# 1. Defining Subgenerators & Composition
# ==========================================

def cluster_alpha_stream():
    """Subgenerator handling primary server zone logs."""
    yield "ALPHA_NODE_01::ONLINE"
    yield "ALPHA_NODE_02::METRICS_CLEAR"
    return "Alpha Stream Completed Successfully" # Return value caught by yield from

def cluster_beta_stream():
    """Subgenerator handling secondary network zone logs."""
    yield "BETA_GATEWAY::ROUTING_ACTIVE"


# ==========================================
# 2. Outer Master Generator Delegation
# ==========================================
def master_log_orchestrator():
    """Orchestrates log streams by delegating control via yield from."""
    print("  [MASTER] Initiating core log diagnostics...")
    
    # Capture the return value directly from the subgenerator execution frame
    alpha_status = yield from cluster_alpha_stream()
    print(f"  [MASTER] Subgenerator status signal received: '{alpha_status}'")
    
    print("  [MASTER] Switching communication proxy channels to Beta zone...")
    yield from cluster_beta_stream()
    
    # yield from can also ingest standard, non-generator collections directly
    print("  [MASTER] Appending static fallback diagnostic markers...")
    yield from ["STATIC_MARKER_A", "STATIC_MARKER_B"]
    
    print("  [MASTER] Core systems diagnostics concluded.")


# ==========================================
# 3. Pipeline Ingestion Execution
# ==========================================
print("--- 1. Executing Delegated Stream Processing ---")

# Instantiate the master orchestrator stream
diagnostic_pipeline = master_log_orchestrator()

# The loop automatically consumes values passed up from the subgenerators
for log_event in diagnostic_pipeline:
    print(f"Consumer Captured Log Event -> {log_event}")