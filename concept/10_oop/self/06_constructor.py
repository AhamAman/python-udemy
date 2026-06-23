class DatabaseConnection:
    """
    Models a defensive database connection configuration.
    Demonstrates how to use constructors as an architectural guardrail.
    """

    def __init__(self, db_name: str, host: str = "localhost", port: int = 5432, max_connections: int = 10):
        """
        The Initializer Constructor.
        
        Args:
          db_name: Required positional parameter (no default value).
          host, port, max_connections: Optional keyword parameters with default values.
        """
        print(f"\n[Constructor] Spawning new DatabaseConnection object for '{db_name}'...")

        # --- 1. GUARANTEED VALIDATION ENGINE ---
        # We perform type and value checks inside the constructor to halt execution 
        # instantly if a developer passes corrupt configuration parameters.
        if not db_name or not isinstance(db_name, str):
            raise ValueError("Initialization Failed: 'db_name' must be a non-empty string.")
            
        if not (1024 <= port <= 65535):
            raise ValueError(f"Initialization Failed: Port {port} is out of safe network ranges.")
            
        if max_connections <= 0:
            raise ValueError("Initialization Failed: Pool must allow at least 1 connection.")

        # --- 2. MULTI-ATTRIBUTE INITIALIZATION ---
        # Once values clear the guardrails, they are structurally bound to the object
        self.db_name = db_name
        self.host = host
        self.port = port
        self.max_pool_size = max_connections
        
        # --- 3. DERIVED / INTERNAL STATE ---
        # Attributes don't have to map 1:1 with parameters. 
        # We initialize internal states completely independent of user input.
        self.is_connected = False
        self.active_connections_list = []
        self.creation_timestamp = "2026-06-23" # Evaluated at runtime instantiation

        print(f"[Constructor] Success: '{self.db_name}' memory initialized cleanly.")


# ==========================================
# RUNNING THE CONSTRUCTOR SYSTEM
# ==========================================
print("--- Phase 1: Successful Initializations ---")

# Instance A: Providing only required positional parameters, relying on defaults for the rest
conn_production = DatabaseConnection(db_name="prod_users")
print(f"Production Config -> Host: {conn_production.host} | Port: {conn_production.port} | Connected: {conn_production.is_connected}")

# Instance B: Overriding specific defaults using keyword arguments
conn_analytics = DatabaseConnection(db_name="analytics_lake", host="10.0.0.45", port=9000, max_connections=50)
print(f"Analytics Config  -> Host: {conn_analytics.host} | Port: {conn_analytics.port} | Max Pool: {conn_analytics.max_pool_size}")


print("\n--- Phase 2: Defensive Failure Guardrails ---")

try:
    # This instantiation attempt breaks our constructor's architectural constraints
    print("Attempting to initialize database with a bad port range...")
    broken_conn = DatabaseConnection(db_name="billing_service", port=80) # Insecure port lower bound
except ValueError as error:
    print(f"❌ Initialization Blocked Safely: {error}")