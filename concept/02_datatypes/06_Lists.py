# ==========================================
# 1. Creation, Indexing, and Slicing
# ==========================================
print("--- List Foundations ---")
# Heterogeneous collection
fruits = ["apple", "banana", "cherry", "date"]

print(f"First fruit: {fruits[0]} | Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")  # ['banana', 'cherry'] (stop is exclusive)

# ==========================================
# 2. Modifying Lists (Adding/Removing)
# ==========================================
print("\n--- Modifying Lists ---")
numbers = [1, 2, 3]

# Appending vs Extending
numbers.append([4, 5])  # Injects the list itself as ONE element
print(f"After append: {numbers}")

numbers = [1, 2, 3]
numbers.extend([4, 5])  # Unpacks and adds elements individually
print(f"After extend: {numbers}")

# Removing
popped_val = numbers.pop(0)
print(f"Popped value: {popped_val} | Remaining list: {numbers}")

# ==========================================
# 3. Sorting (In-Place vs New Object)
# ==========================================
print("\n--- Sorting Behaviors ---")
unordered = [5, 2, 9, 1]

# sorted() returns a new object
new_sorted = sorted(unordered)
print(f"Original after sorted(): {unordered} (Untouched)")
print(f"Returned by sorted():    {new_sorted}")

# .sort() alters the object directly
unordered.sort()
print(f"Original after .sort():   {unordered} (Mutated)")

# ==========================================
# 4. The Copying Trap & Nested Lists
# ==========================================
print("\n--- Nesting & The Copy Trap ---")
matrix = [[1, 2], [3, 4]]
print(f"Accessing matrix[1][0]: {matrix[1][0]}") # Row 1, Col 0 -> 3

# Shallow copy demonstration
original = [[1, 2], 3]
shallow = original.copy()

# Modify an item inside the nested list
shallow[0][0] = 99
print(f"Shallow copy: {shallow}")
print(f"Original list: {original} -> (Whoops! The nested list changed here too!)")

# ==========================================
# 5. List Comprehensions
# ==========================================
print("\n--- List Comprehensions ---")
# Traditional way
squares = []
for x in range(5):
    if x % 2 == 0:
        squares.append(x**2)

# Comprehension way (Faster and shorter)
comp_squares = [x**2 for x in range(5) if x % 2 == 0]
print(f"Loop result:          {squares}")
print(f"Comprehension result: {comp_squares}")


# ==========================================
# 1. Creation and Chained Indexing
# ==========================================
print("--- Grid Navigation ---")
# A 3x3 matrix representing a tic-tac-toe board
# Each sub-list represents a horizontal row
board = [
    ["X", "O", "X"],  # Row 0
    [" ", "X", "O"],  # Row 1
    ["O", " ", "X"]   # Row 2
]

# Accessing a single cell: Row 1, Column 2 ("O")
print(f"Target Cell [1][2]: {board[1][2]}")

# Modifying a single cell in place
board[1][0] = "O" 
print(f"Updated Row 1:      {board[1]}")


# ==========================================
# 2. Iterating Over Nested Structures
# ==========================================
print("\n--- Printing the Grid Structure ---")
# To look at every element, we use nested loops
for row_index, row in enumerate(board):
    print(f"Row {row_index}: {row}")


# ==========================================
# 3. The Deep Copy Fix
# ==========================================
print("\n--- Shallow vs. Deep Copying ---")
import copy

original_matrix = [[1, 2], [3, 4]]

# Method A: Shallow Copy
shallow_version = original_matrix.copy()

# Method B: Deep Copy
deep_version = copy.deepcopy(original_matrix)

# Mutate an item inside the first sub-list of both copies
shallow_version[0][0] = 99
deep_version[0][0] = 777

print(f"Original Matrix: {original_matrix}  <- Affected by the shallow copy mutation!")
print(f"Shallow Copy:    {shallow_version}")
print(f"Deep Copy:       {deep_version}")


# ==========================================
# 4. Flattening via Nested Comprehensions
# ==========================================
print("\n--- Flattening a Matrix ---")
matrix = [[1, 2, 3], [4, 5, 6]]

# Turning a 2D list back into a simple 1D list
# Read it left-to-right as you would write a standard nested loop:
# "for row in matrix" followed by "for item in row"
flattened = [item for row in matrix for item in row]
print(f"Flattened 1D array: {flattened}")