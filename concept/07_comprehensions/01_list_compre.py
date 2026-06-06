menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

# # Loop through each item in the menu
# for my_tea in menu:
#     # Check if the substring "Iced" is present in the current item
#     if "Iced" in my_tea:
#         print(my_tea)

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)