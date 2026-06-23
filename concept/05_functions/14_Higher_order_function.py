# ==========================================
# 1. Functions Accepting Functions (Callbacks)
# ==========================================
print("--- 1. The Callback Pattern ---")

def apply_billing_tax(price):
    return price * 1.15

def process_invoice_pipeline(cart_total, tax_calculator_callback):
    """A Higher-Order Function accepting a behavior callback."""
    # The pipeline manages execution, but delegates the math to the callback
    final_cost = tax_calculator_callback(cart_total)
    return f"Transaction processed. Final Ledger Charge: ${final_cost:.2f}"

# Injecting the billing callback directly into the execution flow
print(process_invoice_pipeline(100.00, apply_billing_tax))


# ==========================================
# 2. Functions Returning Functions (Factories)
# ==========================================
print("\n--- 2. The Function Factory Pattern ---")

def configure_api_client(auth_token):
    """A Higher-Order Function returning a tailored inner function."""
    
    def secure_request(endpoint):
        # The inner function locks down 'auth_token' via a closure
        return f"Sending HTTP GET to /{endpoint} wrapped with Bearer: {auth_token}"
        
    return secure_request

# Generate a customized API request function
gate_client = configure_api_client("SECRET_JWT_TOKEN_99")
print(gate_client("v1/users/profile"))


# ==========================================
# 3. Functional Composition (Pipeline Building)
# ==========================================
print("\n--- 3. Functional Composition ---")

def strip_whitespace(text): return text.strip()
def remove_symbols(text): return text.replace("-", "")
def upgrade_casing(text): return text.upper()

def compose_string_sanitizer(*functions):
    """HOF that stitches an arbitrary chain of functions together."""
    def internal_pipeline(initial_value):
        current_state = initial_value
        for func in functions:
            current_state = func(current_state) # Feeds output of one into the next
        return current_state
    return internal_pipeline

# Create a unified sanitization engine out of three distinct functions
sanitize_serial_number = compose_string_sanitizer(strip_whitespace, remove_symbols, upgrade_casing)

raw_serial = "   sn-889a-002x   "
print(f"Raw Input:  '{raw_serial}'")
print(f"Sanitized:  '{sanitize_serial_number(raw_serial)}'")

