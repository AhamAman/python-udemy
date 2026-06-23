# The traditional way (using a flag variable)
items = ["apple", "banana", "cherry"]
target = "orange"
found = False

for item in items:
    if item == target:
        found = True
        print("Found it!")
        break

if not found:
    print("Item not found in the list.")

# The Pythonic way (Clean and concise)
items = ["apple", "banana", "cherry"]
target = "orange"

for item in items:
    if item == target:
        print("Found it!")
        break
else:
    # This ONLY runs if the loop finished without hitting 'break'
    print("Item not found in the list.")

staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

#else run when no break statement is executed in the loop
for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")