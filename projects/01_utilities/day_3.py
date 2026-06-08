"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ The number must be greater than 0.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid whole number.")

def get_split_shares(names, total_bill):
    print("\nHow would you like to split the bill?")
    print("1. Equally")
    print("2. Custom amounts per person")
    
    choice = input("Choose an option (1 or 2): ").strip()
    shares = {}

    if choice == "2":
        remaining_bill = total_bill
        for i, name in enumerate(names):
            # If it's the last person, automatically assign the remainder to avoid rounding issues
            if i == len(names) - 1:
                print(f"{name} covers the remaining balance: {round(remaining_bill, 2)} rupees")
                shares[name] = round(remaining_bill, 2)
            else:
                while True:
                    amt = get_float(f"Enter amount for {name} (Remaining: {round(remaining_bill, 2)}): ")
                    if amt <= remaining_bill:
                        shares[name] = round(amt, 2)
                        remaining_bill -= amt
                        break
                    print("❌ That amount exceeds the remaining bill total!")
    else:
        # Default even split
        even_share = round(total_bill / len(names), 2)
        for name in names:
            shares[name] = even_share

    return shares

def main():
    print("--- 💸 Bill Splitter Upgrade 💸 ---\n")
    
    num_people = get_int("How many people are there in the group? ")
    names = []

    for i in range(num_people):
        name = input(f"Enter the name of person #{i+1}: ").strip()
        # Handle empty names
        if not name:
            name = f"Person {i+1}"
        names.append(name)

    print("")
    total_bill = get_float("Enter the total bill amount: ")
    
    # Calculate shares based on user choice
    shares = get_split_shares(names, total_bill)

    # Output Results
    print("\n" + "*" * 40)
    print(f"Total Bill: {total_bill} rupees")
    print("*" * 40)
    for name, amount in shares.items():
        print(f"👉 {name} owes: {amount} rupees")
    print("*" * 40)

if __name__ == "__main__":
    main()