import time
import random

# ==========================================
# PACKAGED EXCEPTIONS & SECURITY ERROR LOGS
# ==========================================
class WebGatewayError(Exception): """Base gateway exception.""" pass
class ExternalServiceUnavailable(WebGatewayError): """Target API is offline.""" pass
class SecurityBreachIntercepted(WebGatewayError): """Malicious configuration attempt.""" pass


# ==========================================
# THE STATEFUL CIRCUIT BREAKER CONTROLLER
# ==========================================
class CircuitBreaker:
    """Manages system stability by tracking and blocking failing paths."""
    def __init__(self, failure_threshold: int = 2, cooldown_period: float = 2.0):
        self.failure_threshold = failure_threshold
        self.cooldown_period = cooldown_period
        self.failure_count = 0
        self.state = "CLOSED"  # States: CLOSED, OPEN, HALF-OPEN
        self.last_state_change = time.time()

    def observe_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            print("   [Circuit Breaker 🚨] Failure threshold breached! Tripping circuit to OPEN.")
            self.state = "OPEN"
            self.last_state_change = time.time()

    def observe_success(self):
        """Restores circuit safety baseline."""
        print("   [Circuit Breaker ✅] Successful probe acknowledged. Resetting to CLOSED.")
        self.failure_count = 0
        self.state = "CLOSED"

    def allow_execution(self) -> bool:
        """Evaluates circuit state before allowing outbound network requests."""
        current_time = time.time()
        if self.state == "OPEN":
            # Check if the cooldown period has elapsed
            if current_time - self.last_state_change > self.cooldown_period:
                print("   [Circuit Breaker 🟡] Cooldown period expired. Transitioning to HALF-OPEN...")
                self.state = "HALF-OPEN"
                return True
            return False # Block execution entirely
        return True


# ==========================================
# PRODUCTION APP GATEWAY ENGINE
# ==========================================
class UnifiedPaymentGateway:
    def __init__(self):
        self.circuit_breaker = CircuitBreaker()

    def _call_unstable_third_party_vendor(self, amount: float):
        """Simulates a remote banking API suffering an infrastructure crash."""
        raise IOError("TCP Reset: Remote ledger cluster rejected host handshake.")

    def process_user_checkout(self, user_id: str, payload_str: str):
        print(f"\n>>> Gateway processing checkout request for Client account: '{user_id}'...")
        
        try:
            # 1. FAIL-FAST SECURITY SANITIZATION GATE
            # We explicitly screen input values before allocating transaction contexts.
            if "DROP TABLE" in payload_str.upper() or "../" in payload_str:
                # Security Consideration: Halt early and flag the account signature
                raise SecurityBreachIntercepted("Input payload contains illicit control codes.")

            if not user_id.isalnum():
                raise ValueError("Client format error: Identifier must be purely alphanumeric.")

            # 2. CIRCUIT BREAKER FILTER CHECK
            if not self.circuit_breaker.allow_execution():
                print("   [Gateway Fallback Engine] Circuit is OPEN. Bypassing outbound call completely.")
                # GRACEFUL DEGRADATION: Fall back to localized cache metrics instead of a hard crash
                return {"status": "DEGRADED", "user_message": "System is processing delayed transactions. Balance updated.", "data": "LOCAL_CACHE_SNAPSHOT"}

            # 3. VOLATILE REMOTE OPERATION LOOP
            try:
                self._call_unstable_third_party_vendor(amount=500.00)
                
                # If we make it here, the remote call succeeded
                if self.circuit_breaker.state == "HALF-OPEN":
                    self.circuit_breaker.observe_success()
                return {"status": "SUCCESS", "user_message": "Payment verified safely."}

            except IOError as network_drop:
                print(f"   [Infrastructure Outage Log] Outbound HTTP call dropped: {network_drop}")
                self.circuit_breaker.observe_failure()
                raise ExternalServiceUnavailable("Upstream validation engine timed out.")

        # ==========================================
        # PUBLIC SECURITY & ACTOR BOUNDARY HANDLING
        # ==========================================
        except SecurityBreachIntercepted as threat:
            # Audit log captures full technical details for security operations
            print(f"   [INTERNAL AUDIT LOG 🔴] CRITICAL: Security event on user {user_id}. Details: {threat}")
            # Sanitize the exception text sent back to the user to hide system details
            return {"status": "ACCESS_DENIED", "user_message": "Security Verification Failed: Session terminated."}

        except ExternalServiceUnavailable as outage:
            print(f"   [INTERNAL DIAGNOSTIC LOG] Service exception tracked: {outage}")
            # Clean, non-technical message that protects system architecture details
            return {"status": "SERVICE_DEGRADED", "user_message": "Our payment systems are currently experiencing high volume. Please try again shortly."}

        except ValueError as formatting_issue:
            print(f"   [INTERNAL CLIENT LOG] Format clash: {formatting_issue}")
            return {"status": "BAD_REQUEST", "user_message": "Malformed application data shapes."}


# ==========================================
# DRIVING THE SYSTEM THROUGH FAULT SCENARIOS
# ==========================================
gateway = UnifiedPaymentGateway()

print("--- Scenario A: Handling Security Intrusion Attempts ---")
malicious_payload = "SELECT * FROM orders; DROP TABLE users; --"
response_a = gateway.process_user_checkout("USER101", malicious_payload)
print(f"Public User API Response JSON: {response_a}")


print("\n--- Scenario B: Tripping the Circuit Breaker via Failures ---")
# Request 1: Fails, circuit notes failure count = 1
gateway.process_user_checkout("USER202", "valid_payload_string")
# Request 2: Fails, circuit trips to OPEN
gateway.process_user_checkout("USER202", "valid_payload_string")


print("\n--- Scenario C: Automated Circuit Breaker Isolation (Graceful Degradation) ---")
# Request 3: Circuit is OPEN. The gateway avoids the remote call and degrades gracefully.
response_c = gateway.process_user_checkout("USER202", "valid_payload_string")
print(f"Public User API Response JSON: {response_c}")


print("\n--- Scenario D: Cooling Down and Attempting Recovery ---")
# Sleep to pass the cooldown threshold window
print("Sleeping 2.1 seconds to test half-open probing state...")
time.sleep(2.1)

# Request 4: Circuit moves to HALF-OPEN and tests the waters
# (Since our mock vendor is still offline, it will trip open again)
response_d = gateway.process_user_checkout("USER303", "valid_payload_string")
print(f"Public User API