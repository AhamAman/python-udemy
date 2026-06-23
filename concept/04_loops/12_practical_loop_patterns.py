# --- Counting Pattern ---
# Purpose: Count how many items match a specific condition.
orders = ["shipped", "pending", "shipped", "cancelled", "shipped"]
shipped_count = 0

for status in orders:
    if status == "shipped":
        shipped_count += 1

print(f"Total Shipped Orders: {shipped_count}")


# --- Summation Pattern ---
# Purpose: Calculate a running total of numerical values.
cart_prices = [19.99, 5.50, 102.00, 12.75]
subtotal = 0.0

for price in cart_prices:
    subtotal += price

print(f"Cart Subtotal: ${subtotal:.2f}")

# --- Counting Pattern ---
# Purpose: Count how many items match a specific condition.
orders = ["shipped", "pending", "shipped", "cancelled", "shipped"]
shipped_count = 0

for status in orders:
    if status == "shipped":
        shipped_count += 1

print(f"Total Shipped Orders: {shipped_count}")


# --- Summation Pattern ---
# Purpose: Calculate a running total of numerical values.
cart_prices = [19.99, 5.50, 102.00, 12.75]
subtotal = 0.0

for price in cart_prices:
    subtotal += price

print(f"Cart Subtotal: ${subtotal:.2f}")

# --- Searching Pattern (First Match / Short-circuit) ---
# Purpose: Locate an item and exit early to save processing time.
usernames = ["user10", "admin_test", "dev_core", "guest_90"]
target_admin = None

for user in usernames:
    if user.startswith("admin"):
        target_admin = user
        break  # Exit loop immediately once found

print(f"Found Admin Account: {target_admin}")


# --- Filtering Pattern ---
# Purpose: Extract all elements matching a condition into a new collection.
sensor_readings = [22.1, 45.0, 18.3, 51.2, 23.9, 60.1]
critical_anomalies = []

for reading in sensor_readings:
    if reading > 40.0:  # Threshold limit
        critical_anomalies.append(reading)

print(f"Critical Anomalies Filtered: {critical_anomalies}")

# --- Data Transformation (Mapping) ---
# Purpose: Convert raw data into a structured format.
raw_temperatures_c = [0, 20, 37, 100]
transformed_f = []

for celsius in raw_temperatures_c:
    fahrenheit = (celsius * 9/5) + 32
    transformed_f.append(fahrenheit)

print(f"Temperatures in Fahrenheit: {transformed_f}")


# --- Aggregation Pattern (Find Extrema) ---
# Purpose: Condense a collection down to an aggregate value (like Min/Max).
stock_prices = [142.50, 145.20, 139.80, 141.10, 146.00]

# Initialize with the first element as the benchmark
max_price = stock_prices[0] 

for price in stock_prices:
    if price > max_price:
        max_price = price

print(f"Highest Recorded Stock Price: ${max_price}")

# --- User Input & Validation Loop ---
# Purpose: Repeatedly prompt a user until they provide valid data.
while True:
    user_input = input("Enter a positive number: ").strip()
    
    # Validation step
    if user_input.isdigit() and int(user_input) > 0:
        validated_number = int(user_input)
        print(f"Input accepted: {validated_number}")
        break  # Break out of the infinite loop
    else:
        print("Invalid input. Please try again.")

import time
import random

# Mock function simulating an unstable API network request
def transient_network_api():
    return random.choice([200, 500, 503])  # 200 = Success, 500/503 = Server Errors


# --- Retry Loop (With Backoff Delay) ---
# Purpose: Re-attempt a failing operation a set number of times before failing.
max_retries = 3
backoff_delay = 1  # Time in seconds

print("\n--- Initiating Network Connection Attempt ---")
for attempt in range(1, max_retries + 1):
    status_code = transient_network_api()
    
    if status_code == 200:
        print(f"Attempt {attempt}: Success (200 OK)!")
        break
    else:
        print(f"Attempt {attempt}: Failed with code {status_code}.")
        if attempt < max_retries:
            print(f"Retrying in {backoff_delay} second(s)...")
            time.sleep(backoff_delay)
            backoff_delay *= 2  # Exponential backoff escalation
else:
    # Executed ONLY if the loop finishes naturally without hitting a 'break'
    print("Critical Error: Max retries exhausted. Operation failed.")


# --- Polling Loop ---
# Purpose: Check the status of a long-running process periodically until it completes.
job_status = ["processing", "processing", "processing", "completed"]
job_pointer = 0

print("\n--- Polling Server for Background Job Completion ---")
while True:
    # Query current state
    current_state = job_status[job_pointer]
    print(f"Checking status... Current state: '{current_state}'")
    
    if current_state == "completed":
        print("Job done! Downloading assets...")
        break
        
    job_pointer += 1
    time.sleep(1)  # Throttle polling frequency to prevent server spamming


