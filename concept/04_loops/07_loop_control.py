# --- DEMO 1: The 'break' statement (Searching for an item) ---
print("--- BREAK DEMO ---")
shopping_list = ["apples", "milk", "CHOPPED TOMATOES", "bread", "eggs"]

for item in shopping_list:
    if item == "CHOPPED TOMATOES":
        print(f"Found {item}! Stopping the search.")
        break  # Exits the loop entirely
    print(f"Checking item: {item}")

print("Loop finished. Moving on to the next task.\n")


# --- DEMO 2: The 'continue' statement (Filtering out data) ---
print("--- CONTINUE DEMO ---")
numbers = [1, -2, 3, -4, 5, -6]
positive_sum = 0

for num in numbers:
    if num < 0:
        print(f"Skipping negative number: {num}")
        continue  # Skips the rest of this iteration, jumps to next number
    
    # This part only runs if num >= 0
    positive_sum += num
    print(f"Adding {num} to the total.")

print(f"Total sum of positives: {positive_sum}\n")


# --- DEMO 3: The 'pass' statement (The Placeholder) ---
print("--- PASS DEMO ---")
for x in range(3):
    if x == 1:
        # TODO: Implement special handling for 1 later
        pass  # Keeps Python happy without changing execution
    print(f"Processing number: {x}")