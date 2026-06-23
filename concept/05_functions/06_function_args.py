# ==========================================
# 1. Signature Boundaries (/ and *)
# ==========================================
def configure_system(mode, /, threshold=0.5, *, alert_email):
    """
    'mode' is POSITIONAL-ONLY (to the left of /).
    'threshold' can be passed either way.
    'alert_email' is KEYWORD-ONLY (to the right of *).
    """
    print(f"System Mode: {mode} | Threshold: {threshold} | Alerting: {alert_email}")

# Valid Call
configure_system("ACTIVE", 0.8, alert_email="ops@infra.net")

# Invalid Call Scenario A (Trying to pass keyword for positional-only)
try:
    configure_system(mode="ACTIVE", alert_email="ops@infra.net")
except TypeError as err:
    print(f"Caught expected Positional-Only Violation: {err}")

# Invalid Call Scenario B (Trying to pass positional for keyword-only)
try:
    configure_system("ACTIVE", 0.8, "ops@infra.net")
except TypeError as err:
    print(f"Caught expected Keyword-Only Violation: {err}")


# ==========================================
# 2. Dynamic Packing (*args and **kwargs)
# ==========================================
print("\n--- Variable-Length Packing ---")

def pipeline_logger(log_level, *args, **kwargs):
    # args captures extra positional arguments as a Tuple
    print(f"[{log_level}] Unstructured Metadata: {args} | Type: {type(args)}")
    # kwargs captures extra keyword arguments as a Dict
    print(f"[{log_level}] Structured Context:    {kwargs} | Type: {type(kwargs)}")

pipeline_logger("CRITICAL", "Disk_Failure", "Sector_4", node_id=1099, cluster="us-east")


# ==========================================
# 3. Argument Forwarding & Unpacking
# ==========================================
print("\n--- Unpacking and Forwarding Patterns ---")

def raw_destination(a, b, c):
    print(f"Destination Target received values: a={a}, b={b}, c={c}")

# Unpacking vectors at the call site
scalar_list = [10, 20, 30]
keyword_dict = {"a": 1, "b": 2, "c": 3}

# List Unpacking -> Becomes raw_destination(10, 20, 30)
raw_destination(*scalar_list)

# Dictionary Unpacking -> Becomes raw_destination(a=1, b=2, c=3)
raw_destination(**keyword_dict)


print("\n--- Proxy Forwarding Wrapper ---")
# The universal wrapper pattern
def proxy_wrapper(*args, **kwargs):
    print("Proxy Interceptor: Logging execution metrics...")
    # Forwarding the payloads completely intact
    return raw_destination(*args, **kwargs)

proxy_wrapper(100, b=200, c=300)