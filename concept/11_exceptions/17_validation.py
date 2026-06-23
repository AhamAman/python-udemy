import json
import re

# ==========================================
# CUSTOM VALIDATION EXCEPTION DOMAIN
# ==========================================
class ValidationError(Exception): """Base exception for all system validation faults.""" pass
class InvalidPayloadStructure(ValidationError): """Thrown when request data shapes are corrupt.""" pass
class ConfigurationFault(ValidationError): """Thrown when boot settings are invalid.""" pass
class BusinessRuleViolation(ValidationError): """Thrown when data breaks domain invariants.""" pass


# ==========================================
# 1. CONFIGURATION LAYER VALIDATION
# ==========================================
class SystemConfiguration:
    """Validates global environmental boundaries at application boot time."""
    def __init__(self, env_settings: dict):
        print("[Boot Sync] Running System Configuration Validation...")
        
        # Guardrail: Check for required infrastructure variables
        if "api_version" not in env_settings:
            raise ConfigurationFault("System Boot Aborted: Missing required key 'api_version'.")
            
        if env_settings["max_transaction_limit"] <= 0:
            raise ConfigurationFault("System Boot Aborted: 'max_transaction_limit' must be a positive threshold.")
            
        self.version = env_settings["api_version"]
        self.max_limit = float(env_settings["max_transaction_limit"])
        print("   [Boot Success] System parameters verified and locked.")


# ==========================================
# 2. CORE BUSINESS DOMAIN LAYER VALIDATION
# ==========================================
class LedgerTransaction:
    """Enforces deep contextual business rules on validated objects."""
    def __init__(self, sender_id: str, amount: float):
        self.sender_id = sender_id
        self.amount = amount

    def evaluate_business_invariants(self, current_sender_balance: float, system_max: float):
        """Validates contextual logic that cannot be checked by type definitions alone."""
        print(f"   [Domain Engine] Evaluating business invariants for sender '{self.sender_id}'...")
        
        # Business Rule 1: Individual transaction caps
        if self.amount > system_max:
            raise BusinessRuleViolation(
                f"Limit Breach: Requested transaction amount (${self.amount:.2f}) "
                f"exceeds system threshold limits (${system_max:.2f})."
            )
            
        # Business Rule 2: Overdraft boundaries
        if self.amount > current_sender_balance:
            raise BusinessRuleViolation(
                f"Insufficient Capital: Attempted to draw ${self.amount:.2f} "
                f"from account balance of ${current_sender_balance:.2f}."
            )
            
        print("   [Domain Engine] All business logic checks cleared safely.")
        return "PROCESSED"


# ==========================================
# 3. OUTER API REQUEST / USER INPUT VALIDATION
# ==========================================
class TransactionIngestionGateway:
    """The outer system edge: intercepting raw, untrusted data shapes."""
    def __init__(self, system_config: SystemConfiguration):
        self.config = system_config
        # Simple regex tracking alphanumeric user account structures (e.g., ACC-12345)
        self.account_pattern = re.compile(r"^ACC-\d{5}$")

    def process_incoming_json_post(self, raw_untrusted_json: str, sender_live_balance: float):
        print(f"\n>>> API Ingestion Gateway parsing incoming string body payload...")
        
        try:
            # Step A: Structural Validation
            try:
                payload = json.loads(raw_untrusted_json)
            except json.JSONDecodeError as json_err:
                raise InvalidPayloadStructure(f"Malformed API Body payload. Invalid JSON syntax: {json_err}")

            # Step B: Schema Data Validation (Type and Presence checking)
            required_fields = ["account_id", "amount"]
            for field in required_fields:
                if field not in payload:
                    raise InvalidPayloadStructure(f"Schema Violation: Missing required field '{field}'.")

            account_token = payload["account_id"]
            amount_value = payload["amount"]

            # Step C: User Input Sanitization Check (Pattern verification)
            if not isinstance(account_token, str) or not self.account_pattern.match(account_token):
                raise InvalidPayloadStructure(f"Format Violation: Field 'account_id' must match pattern 'ACC-XXXXX'.")

            if not isinstance(amount_value, (int, float)):
                raise InvalidPayloadStructure("Type Violation: Field 'amount' must be a numeric integer or float.")

            print("   [Gateway Success] Outer API structural validation passed. Handing off to domain space...")

            # Step D: Handoff to Business Domain Layer
            domain_model = LedgerTransaction(sender_id=account_token, amount=float(amount_value))
            result = domain_model.evaluate_business_invariants(
                current_sender_balance=sender_live_balance,
                system_max=self.config.max_limit
            )
            return result

        # Catch-all exception routing for the gateway boundary
        except ValidationError as validation_fault:
            print(f"❌ Ingestion Intercepted & Blocked: {type(validation_fault).__name__}")
            print(f"   Rejection Diagnostics: {validation_fault}")
            return "TRANSACTION_REJECTED"


# ==========================================
# RUNNING THE VALIDATION TEST PIPELINE
# ==========================================

# Initialize system configuration setting thresholds
runtime_settings = {"api_version": "v4.2-prod", "max_transaction_limit": 50000.00}
global_config = SystemConfiguration(runtime_settings)
gateway = TransactionIngestionGateway(global_config)


print("\n--- Case A: Pristine Structural and Domain Pass ---")
good_payload = '{"account_id": "ACC-10442", "amount": 1500.00}'
status_a = gateway.process_incoming_json_post(good_payload, sender_live_balance=8000.00)
print(f"Gateway Response Code: {status_a}")


print("\n--- Case B: Outer API Structural Failure (Syntax Error) ---")
broken_json = '{"account_id": "ACC-10442", "amount": 1500.00' # Missing closing curly bracket
status_b = gateway.process_incoming_json_post(broken_json, sender_live_balance=8000.00)
print(f"Gateway Response Code: {status_b}")


print("\n--- Case C: Outer User Input Failure (Regex Pattern Clash) ---")
bad_user_input = '{"account_id": "MALICIOUS_SQL_INJECTION_STRING", "amount": 100.00}'
status_c = gateway.process_incoming_json_post(bad_user_input, sender_live_balance=8000.00)
print(f"Gateway Response Code: {status_c}")


print("\n--- Case D: Inner Core Business Rule Failure (Overdraft) ---")
overdraft_payload = '{"account_id": "ACC-99211", "amount": 45000.00}'
# Payload structure passes API schema verification, but crashes inside business layer limits
status_d = gateway.process_incoming_json_post(overdraft_payload, sender_live_balance=2000.00)
print(f"Gateway Response Code: {status_d}")