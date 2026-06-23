import sys

# ==========================================
# CUSTOM DB PROTOCOL EXCEPTION SIMULATORS
# ==========================================
class DatabaseError(Exception): """Generic database engine parent class.""" pass
class DBConnectionError(DatabaseError): """Database connection handshake dropped.""" pass
class OperationalError(DatabaseError): """Internal engine anomalies like Deadlocks.""" pass
class IntegrityError(DatabaseError): """Data schema constraint boundary violated.""" pass


class MockDatabaseConnectionEngine:
    """Simulates a live persistent ACID-compliant SQL engine channel."""
    def __init__(self):
        self.in_transaction = False
        self.connection_active = True

    def begin_transaction(self):
        if not self.connection_active:
            raise DBConnectionError("CRITICAL: Lost communication link to master storage cluster.")
        print("   [Engine Engine] ACID Transaction isolation lock established.")
        self.in_transaction = True

    def execute_query(self, sql_statement: str, parameters: dict):
        if not self.in_transaction:
            raise OperationalError("Illegal State: Cannot mutate data blocks outside an active transaction context.")
        
        print(f"      [SQL Query Executing] {sql_statement} | Binding: {parameters}")
        
        # Simulate an integrity violation (Unique Key Constraint Clash)
        if parameters.get("user_id") == "DUPLICATE_ID":
            raise IntegrityError("SQL Error 1062: Duplicate entry detected for Unique Key constraint 'PRIMARY'.")
            
        # Simulate an internal transaction deadlock collision
        if parameters.get("amount", 0) > 1000000:
            raise OperationalError("SQL Error 1213: Deadlock found when trying to get lock; try restarting transaction.")

    def commit(self):
        print("   [Engine Engine] 💾 Changes permanently flushed to non-volatile disk. Releasing transaction locks.")
        self.in_transaction = False

    def rollback(self):
        if self.in_transaction:
            print("   [Engine Engine] 🔄 ROLLBACK TRIGGERED: Restoring database state blocks to initial checkpoint snapshot.")
            self.in_transaction = False

    def close(self):
        print("   [Engine Engine] Connection handle safely recycled back to pool manager.")
        self.connection_active = False


# ==========================================
# SAFE TRANSACTION UNIT IMPLEMENTATION
# ==========================================

def process_secure_ledger_transfer(db_engine: MockDatabaseConnectionEngine, from_user: str, to_user: str, amount: float):
    print(f"\n>>> Initializing Secure Ledger Entry: Transferring ${amount:.2f} from '{from_user}' to '{to_user}'")
    
    try:
        # Step 1: Open the transaction boundaries
        db_engine.begin_transaction()
        
        # Step 2: Dispatch query operations
        db_engine.execute_query(
            "UPDATE accounts SET balance = balance - :amount WHERE user_id = :user_id", 
            {"user_id": from_user, "amount": amount}
        )
        db_engine.execute_query(
            "UPDATE accounts SET balance = balance + :amount WHERE user_id = :user_id", 
            {"user_id": to_user, "amount": amount}
        )

    # ==========================================
    # CATCHING DIVERGENT DATABASE THREATS
    # ==========================================
    except IntegrityError as schema_clash:
        print(f"   [Transaction Blocked] Relational Contradiction Encountered: {schema_clash}")
        # Automatically reverse mutations to keep data sets pristine
        db_engine.rollback()
        return "REJECTED_BAD_DATA"

    except OperationalError as dead_lock:
        print(f"   [Transaction Blocked] Transient Engine Deadlock Intercepted: {dead_lock}")
        print("   [System Recovery Engine] Registering task back onto retry queue...")
        db_engine.rollback()
        return "RETRY_QUEUED"

    except DBConnectionError as connection_drop:
        print(f"   [Infrastructure Outage] Network Layer Collapsed: {connection_drop}")
        # Note: Rollback is impossible if the connection cable is physically severed,
        # but the DB engine will automatically time out and discard our uncommitted changes.
        return "POOL_DISCONNECTED"

    else:
        # The Else block executes ONLY if every single statement in the Try block ran perfectly.
        # This guarantees we never commit a partial transaction block!
        db_engine.commit()
        return "TRANSACTION_SUCCESS"

    finally:
        # Enforce guaranteed clean up of physical hardware handles
        db_engine.close()


# ==========================================
# EXECUTING TRANSACTION SCENARIOS
# ==========================================
print("--- Run 1: Flawless Ledger Entry ---")
db_pool_alpha = MockDatabaseConnectionEngine()
status_one = process_secure_ledger_transfer(db_pool_alpha, "USER-101", "USER-202", 250.00)
print(f"Workflow Outcome Code: {status_one}")


print("\n--- Run 2: Trapping an Integrity Error Constraint Break ---")
db_pool_beta = MockDatabaseConnectionEngine()
# Passing a duplicate user key trips the Integrity Error gate
status_two = process_secure_ledger_transfer(db_pool_beta, "DUPLICATE_ID", "USER-202", 10.00)
print(f"Workflow Outcome Code: {status_two}")


print("\n--- Run 3: Suriving a Resource Deadlock Lock ---")
db_pool_gamma = MockDatabaseConnectionEngine()
# Requesting an excessive amount triggers an inner engine lock contention
status_three = process_secure_ledger_transfer(db_pool_gamma, "USER-101", "USER-202", 5000000.00)
print(f"Workflow Outcome Code: {status_three}")