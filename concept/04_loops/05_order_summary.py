names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

# loop thriugh both lists at the same time using zip
for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")