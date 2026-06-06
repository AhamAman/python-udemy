#input - gives string, so we need to convert it to int

order_amount = int(input("Enter the order amount: "))

#ternary operator - single line if else statement
delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")