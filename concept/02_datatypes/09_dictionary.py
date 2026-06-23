# ==========================================
# 1. Creation, Keys, and Safe Access
# ==========================================
print("--- Dictionary Basics ---")
user_data = {
    "username": "coder_99",
    "status": "active",
    "login_count": 5
}

# Accessing values
print(f"Username: {user_data['username']}")

# Safe access with .get() to prevent crashes
print(f"Theme selection: {user_data.get('theme', 'default_dark')}") 

# ==========================================
# 2. Mutating Entries & View Objects
# ==========================================
print("\n--- Mutations & View Objects ---")
# Get a live view of the keys
all_keys = user_data.keys()
print(f"Keys before update: {all_keys}")

# Updating an existing key, and adding a new one
user_data["login_count"] = 6
user_data["is_admin"] = False

# The view object reflects changes instantly without calling .keys() again!
print(f"Keys after update:  {all_keys}")

# Using .items() to unpack keys and values simultaneously
for key, value in user_data.items():
    print(f"  Field: {key:12} -> Value: {value}")

# ==========================================
# 3. Dictionary Comprehensions
# ==========================================
print("\n--- Dictionary Comprehensions ---")
stocks = {"AAPL": 150, "GOOG": 2800, "TSLA": 700}

# Create a new filtered dict where values are altered
discount_stocks = {ticker: price * 0.9 for ticker, price in stocks.items() if price > 200}
print(f"Premium stocks (10% off): {discount_stocks}")

# ==========================================
# 4. Nested Dictionaries
# ==========================================
print("\n--- Nested Architecture ---")
# Simulating a JSON API payload
corporate_network = {
    "hq": {
        "location": "New York",
        "servers": ["srv-auth", "srv-db"]
    },
    "branch": {
        "location": "London",
        "servers": ["srv-edge"]
    }
}

# Chained brackets to drill deep down the layers
print(f"HQ Main Database Server: {corporate_network['hq']['servers'][1]}")

