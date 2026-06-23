import time
import random

# ==========================================
# CUSTOM NETWORK EXCEPTION SIMULATORS
# ==========================================
class NetworkGatewayError(IOError): """Base network failure.""" pass
class RemoteTimeoutError(NetworkGatewayError): """Target timed out.""" pass
class RateLimitExceededError(NetworkGatewayError): """HTTP 429 Too Many Requests.""" pass


class MockAPIInfrastructure:
    """Simulates an unpredictable remote web server container."""
    def __init__(self):
        self.request_counter = 0

    def dispatch_http_request(self, endpoint: str):
        self.request_counter += 1
        print(f"      [Server Wire] Intercepting connection to '{endpoint}' (Attempt {self.request_counter})...")
        
        # Simulate an initial transient timeout drop
        if self.request_counter == 1:
            raise RemoteTimeoutError("Connection dropped: Remote gateway failed to respond.")
            
        # Simulate a transient downstream rate-limit spike
        if self.request_counter == 2:
            raise RateLimitExceededError("HTTP Error 429: Rate limit capacity exceeded.")
            
        # Success path reached on attempt 3
        print("      [Server Wire] 200 OK Response generated successfully.")
        return {"status": "SUCCESS", "telemetry_payload": [45.2, 88.1, 12.9]}


# ==========================================
# RESILIENT CLIENT IMPLEMENTATION
# ==========================================

def execute_resilient_get(api_server: MockAPIInfrastructure, endpoint: str, max_retries: int = 3):
    """
    Executes a network call wrapped in an Exponential Backoff retry loop
    with randomized jitter to maximize distributed architecture survival.
    """
    base_backoff_seconds = 1.0
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"   [Client] Initiating request pipeline window...")
            # We pass explicit timeout parameters down to our network socket layers
            response = api_server.dispatch_http_request(endpoint)
            return response # If successful, break out instantly and return data

        # ==========================================
        # TARGETED TRANSIENT NETWORK CATCHING
        # ==========================================
        except (RemoteTimeoutError, RateLimitExceededError) as transient_fault:
            print(f"   [Client ⚠️] Transient Network Exception Intercepted: {transient_fault}")
            
            if attempt == max_retries:
                print("   [Client ❌] Maximum retry thresholds exhausted. Aborting propagation loops.")
                raise NetworkGatewayError("Catastrophic Pipeline Breakage: Upstream network completely unreachable.")

            # --------------------------------------
            # EXPONENTIAL BACKOFF WITH JITTER MOTOR
            # --------------------------------------
            # Formula: Backoff = Base * 2^(attempt-1)
            # Jitter adds a randomized offset to prevent "Thundering Herd" syndrome.
            backoff_delay = base_backoff_seconds * (2 ** (attempt - 1))
            jittered_delay = backoff_delay + random.uniform(0.1, 0.5)
            
            print(f"   [Client] Backoff Strategy Engaged: Sleeping for {jittered_delay:.2f}s before retry...")
            time.sleep(jittered_delay)


# ==========================================
# EXECUTING HIGH-RESILIENCE TEST PASS
# ==========================================
print("--- Phase 1: Executing Fault-Tolerant Distributed Request ---")
remote_cluster = MockAPIInfrastructure()

try:
    # The client handles early failures seamlessly under the hood
    data_packet = execute_resilient_get(remote_cluster, endpoint="/v2/metrics/stream")
    print(f"\nFinal Extracted Client Data: {data_packet}")
except NetworkGatewayError as fatal_drop:
    print(f"\nTerminal Application Warning: {fatal_drop}")