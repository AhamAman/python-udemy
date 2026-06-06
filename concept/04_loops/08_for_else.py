staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

#else run when no break statement is executed in the loop
for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")