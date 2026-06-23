# ==========================================
# 1. Cartesian Product & Loop Sequencing
# ==========================================
print("--- 1. Cartesian Coordinate Space ---")

axes_x = ["X1", "X2"]
axes_y = ["Y1", "Y2", "Y3"]

# Target: Find every possible combination between X and Y axes
# Sequential Rule: Outer loop first, Inner loop second (Left-to-Right)
cartesian_product = [(x, y) for x in axes_x for y in axes_y]

print(f"Generated Cartesian Matrix Space:\n  {cartesian_product}")


# ==========================================
# 2. Flattening a High-Dimensional Matrix
# ==========================================
print("\n--- 2. Unrolling Matrix Layers ---")

# A 2D array representation (3x3 Matrix)
matrix_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traditional Imperative Equivalence:
# flat_list = []
# for row in matrix_grid:         <-- Outer Loop
#     for item in row:           <-- Inner Loop
#         flat_list.append(item)

# Linear Translation: Match the exact vertical loop setup from left to right
flattened_array = [item for row in matrix_grid for item in row]
print(f"Flattened Array Stream: {flattened_array}")


# ==========================================
# 3. Grid Generation (Nested Array Building)
# ==========================================
print("\n--- 3. 2D Coordinate Grid Generation ---")

# Target: Generate an empty identity game board or matrix grid (3 rows, 4 columns filled with zeroes)
# Here, the expression slot on the left IS its own standalone comprehension.
grid_3x4 = [[0 for _ in range(4)] for _ in range(3)]

print("Generated 3x4 Hardware Grid Matrix Layout:")
for row in grid_3x4:
    print(f"  {row}")


# ==========================================
# 4. Complex Matrix Filtering and Traversal
# ==========================================
print("\n--- 4. Complex Multi-Dimensional Filtering ---")

# Target: Traverse our matrix_grid and extract only EVEN numbers
# You can place filtering conditions right after the inner loop evaluation
even_matrix_elements = [
    item 
    for row in matrix_grid 
    for item in row 
    if item % 2 == 0
]
print(f"Extracted Even Elements: {even_matrix_elements}")
