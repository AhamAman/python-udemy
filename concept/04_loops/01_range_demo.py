import sys

print("--- 1. Single Argument: range(stop) ---")
# Starts at 0, ends before 5
for i in range(5):
    print(i, end=" ")  # Outputs: 0 1 2 3 4
print("\n")

print("--- 2. Two Arguments: range(start, stop) ---")
# Starts at 5, ends before 10
for i in range(5, 10):
    print(i, end=" ")  # Outputs: 5 6 7 8 9
print("\n")

print("--- 3. Three Arguments: range(start, stop, step) ---")
# Starts at 0, steps by 2, ends before 10
for i in range(0, 10, 2):
    print(i, end=" ")  # Outputs: 0 2 4 6 8
print("\n")

print("--- 4. Reverse Iteration: Negative Steps ---")
# Starts at 10, steps down by -2, ends before 0 (exclusive, so stops at 2)
for i in range(10, 0, -2):
    print(i, end=" ")  # Outputs: 10 8 6 4 2
print("\n")

print("--- 5. Proof: range is NOT a list ---")
small_range = range(10)
huge_range = range(1000000000)  # One billion numbers!

print(f"Type of small_range: {type(small_range)}")
print(f"Printing the range object directly: {small_range}")

print("\n--- 6. Memory Efficiency Analysis ---")
# Checking the actual size in bytes using sys.getsizeof()
size_small = sys.getsizeof(small_range)
size_huge = sys.getsizeof(huge_range)

print(f"Memory size of range(10):          {size_small} bytes")
print(f"Memory size of range(1000000000):  {size_huge} bytes")
print("Notice they take up the exact same amount of memory!")

# Converting to an actual list forces Python to allocate memory for every integer
actual_list = list(range(1000))
print(f"Memory size of actual list(1000):  {sys.getsizeof(actual_list)} bytes")

print("\nDemo complete!")