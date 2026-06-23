# ==========================================
# 1. The Complex "Pyramid of Doom" Approach
# ==========================================
print("--- The Deeply Nested Anti-Pattern ---")

def process_payment_nested(user_logged_in, cart_has_items, card_valid):
    # Layer 1
    if user_logged_in:
        # Layer 2
        if cart_has_items:
            # Layer 3 (Deep pyramid forming)
            if card_valid:
                return "Payment successful! Items shipped."
            else:
                return "Error: Credit card authorization failed."
        else:
            return "Error: Shopping cart is empty."
    else:
        return "Error: User session unauthenticated."

print(process_payment_nested(True, True, False))


# ==========================================
# 2. Refactored Flat Architecture (Guard Clauses)
# ==========================================
print("\n--- Flattened Refactoring via Guard Clauses ---")

def process_payment_flat(user_logged_in, cart_has_items, card_valid):
    # Guard 1: Check authentication instantly and bounce out
    if not user_logged_in:
        return "Error: User session unauthenticated."
        
    # Guard 2: Check contents and bounce out
    if not cart_has_items:
        return "Error: Shopping cart is empty."
        
    # Guard 3: Check funds and bounce out
    if not card_valid:
        return "Error: Credit card authorization failed."
        
    # The 'Happy Path' remains completely un-nested at the base level!
    return "Payment successful! Items shipped."

print(process_payment_flat(True, True, True))


# ==========================================
# 3. Simplification via Logical Combination
# ==========================================
print("\n--- Flattened via Logical and Operators ---")
is_weekend = True
has_free_time = True

# Nested Way:
# if is_weekend:
#     if has_free_time:
#         print("Go explore the outdoors.")

# Flat Way:
if is_weekend and has_free_time:
    print("Action Plan: Go explore the outdoors.")