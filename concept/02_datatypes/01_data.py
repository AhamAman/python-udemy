# ==========================================
# 1. Variables, Values, and Dynamic Typing
# ==========================================

# 'box' is a variable pointing to an integer object containing the value 42
box = 42
print(f"Value: {box}, Type: {type(box)}")

# Dynamic Typing: We can reassign 'box' to point to a completely different type of object
box = "Hello World"
print(f"Value: {box}, Type: {type(box)}")


# ==========================================
# 2. Types Dictate Allowed Operations
# ==========================================
num1 = 10
num2 = 20
text1 = "Python "
text2 = "Rocks"

# The '+' operator means ARITHMETIC ADDITION for integers
print("\nOperation on ints (+):", num1 + num2)  # Outputs: 30

# The '+' operator means STRING CONCATENATION for strings
print("Operation on strings (+):", text1 + text2)  # Outputs: Python Rocks


# ==========================================
# 3. What Type Safety Prevents (Runtime Error)
# ==========================================
print("\nAttempting an invalid operation...")
try:
    # This will crash because you cannot add text to a number.
    # Python checks the types at runtime and raises a TypeError.
    invalid_operation = text1 + num1
except TypeError as error:
    print(f"Caught an expected error: {error}")

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


