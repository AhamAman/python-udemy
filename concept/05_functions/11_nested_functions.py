# ==========================================
# 1. Encapsulation & The Helper Pattern
# ==========================================
print("--- 1. Encapsulated Sub-Routines ---")

def process_sensor_matrix(raw_voltages):
    """Primary algorithm exposed to the wider application."""
    
    # Encapsulated inner function: completely hidden from the outside world
    def calculate_celsius(voltage):
        return (voltage * 0.1) - 4.2
        
    # The outer function orchestrates operations using the hidden helper
    processed_temperatures = [calculate_celsius(v) for v in raw_voltages]
    return processed_temperatures

# Execution
metrics = [240, 510, 890]
print(f"Processed Results: {process_sensor_matrix(metrics)}")

try:
    # This will crash instantly because the helper function is safely trapped inside local scope
    calculate_celsius(300)
except NameError as err:
    print(f"Caught expected security guardrail: {err}")


# ==========================================
# 2. State Retention & Closures
# ==========================================
print("\n--- 2. Persistent Closure States ---")

def initialize_database_session(environment_tier):
    """Outer factory function that sets a persistent structural parameter."""
    connection_string = f"db://cluster.internal/{environment_tier}"
    
    # Inner function tracks the variables in its enclosing scope
    def run_query(sql_statement):
        # Even after initialize_database_session finishes, run_query retains connection_string
        return f"Executing [{sql_statement}] against endpoint: {connection_string}"
        
    return run_query # Returning the unexecuted function object itself

# Construct two independent database query engines with locked-in states
prod_db = initialize_database_session("PRODUCTION")
staging_db = initialize_database_session("STAGING")

# The parent function frame is dead, but the inner functions remember their environments perfectly:
print(prod_db("SELECT * FROM users;"))
print(staging_db("SELECT * FROM testing_metrics;"))