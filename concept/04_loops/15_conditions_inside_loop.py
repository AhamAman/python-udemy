import time

def separator(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# =====================================================================
# 1. USING IF INSIDE A FOR LOOP (Filtering Iterations)
# =====================================================================
separator("1. Filtering with IF inside FOR")

transactions = [120.50, -20.00, 45.00, -5.25, 300.00]
print("Processing only positive credit earnings:")

for amount in transactions:
    if amount > 0:
        print(f"  Credited: ${amount:.2f}")
    else:
        print("  [Debits are ignored in this run]")


# =====================================================================
# 2. USING IF INSIDE A WHILE LOOP (State Monitoring)
# =====================================================================
separator("2. State Tracking with IF inside WHILE")

fuel_level = 100
while fuel_level > 0:
    fuel_level -= 30
    
    if fuel_level <= 40 and fuel_level > 0:
        print(f"  Warning: Fuel low! Current level: {fuel_level}%")
    elif fuel_level <= 0:
        print("  Warning: Fuel exhausted! Tank empty.")
    else:
        print(f"  Cruising status stable. Fuel at: {fuel_level}%")


# =====================================================================
# 3. CONDITIONAL CONTINUE & BREAK
# =====================================================================
separator("3. Conditional Break & Continue")

# Target scenario: Scan a server log file list
log_events = ["INFO: User login", "SKIP: Internal ping", "ERROR: DB Crash", "INFO: Logout"]

print("Starting log event scan...")
for event in log_events:
    # Conditional Continue: Skip unneeded processing
    if event.startswith("SKIP"):
        print("  (Skipping background noise ping...)")
        continue  # Aborts this item, loops back to top for next event
        
    print(f"  Processing critical item: {event}")
    
    # Conditional Break: Critical system emergency halt
    if "ERROR" in event:
        print("  [CRITICAL ALERT] Found Server Crash Error! Halting scanner loop immediately.")
        break  # Completely kills the loop right here


# =====================================================================
# 4. SEARCH ALGORITHMS USING CONDITIONALS
# =====================================================================
separator("4. Search Algorithm (Linear Search)")

catalog = [
    {"id": 101, "item": "Laptop", "in_stock": True},
    {"id": 102, "item": "Mechanical Keyboard", "in_stock": False},
    {"id": 103, "item": "Wireless Mouse", "in_stock": True},
    {"id": 104, "item": "USB-C Cable", "in_stock": True}
]

search_target = "Wireless Mouse"
found_item = None

print(f"Searching database for target: '{search_target}'...")
for product in catalog:
    # Check 1: Does the item match?
    if product["item"] == search_target:
        # Check 2: Nesting a conditional to evaluate inventory state
        if product["in_stock"]:
            found_item = product
            break  # Target acquired! Stop searching the remainder of the list

if found_item:
    print(f"Success! Found item record: {found_item}")
else:
    print("Item could not be found or is out of stock.")

separator("Execution Complete")