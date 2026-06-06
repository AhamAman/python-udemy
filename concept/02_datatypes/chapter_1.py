'''
Lesson - variable are labels that point to objects in memory. When we assign a value to a variable, we are creating an object in memory and the variable is pointing to that object. When we reassign a variable, we are creating a new object in memory and the variable is now pointing to the new object. This is why the ID of the variable changes when we reassign it. In Python, small integers are cached and reused, so they may have the same ID, but larger integers and other objects will have different IDs when reassigned.

'''

sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

#now see the label chnages to new object in memory
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

x = 6
y = 6

print(f"ID of x: {id(x)}")
print(f"ID of y: {id(y)}")

print('Does x and y refer to same thing?', x is y)


