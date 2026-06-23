# ==========================================
# 1. Creation and Immutability
# ==========================================
print("--- Tuple Basics ---")
# Parentheses are optional but recommended
coordinate = (40.7128, -74.0060) 
print(f"Type: {type(coordinate)} | Value: {coordinate}")

# Proving Immutability
try:
    coordinate[0] = 34.0522  # This will fail
except TypeError as error:
    print(f"Caught expected error: {error}")

# The Deep/Shallow Catch: A mutable list INSIDE an immutable tuple
flexible_tuple = (1, 2, [3, 4])
flexible_tuple[2][0] = 99  # Works! The list modified its own contents.
print(f"Modified inner list: {flexible_tuple}")


# ==========================================
# 2. Unpacking & Variable Swapping
# ==========================================
print("\n--- Unpacking & Swapping ---")
user_profile = ("Alice", 28, "Engineer")

# Unpacking elements into descriptive variable names
name, age, profession = user_profile
print(f"Unpacked -> Name: {name}, Profession: {profession}")

# Multiple Assignment / Value Swapping via implicit tuples
a = 10
b = 20
a, b = b, a  # Python creates a temporary tuple (b, a) then unpacks it into a, b
print(f"Swapped values -> a: {a}, b: {b}")


# ==========================================
# 3. Performance Overhead Comparison
# ==========================================
print("\n--- Performance Overheads ---")
import sys

# Creating a list and tuple with the exact same items
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print(f"List memory footprint:  {sys.getsizeof(list_example)} bytes")
print(f"Tuple memory footprint: {sys.getsizeof(tuple_example)} bytes")


# ==========================================
# 4. Self-Documenting Data: Named Tuples
# ==========================================
print("\n--- Named Tuples ---")
from collections import namedtuple

# Create a custom tuple subclass named 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

pt1 = Point(10.5, 20.3)
print(f"Named Tuple Object: {pt1}")
print(f"Accessing via attribute (.x): {pt1.x}")
print(f"Accessing via index ([1]):    {pt1[1]}")

