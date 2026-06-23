# =====================================================================
# CHEAT SHEET: PYTHON FLOATING-POINT LIMITATIONS (IEEE 754 STANDARD)
# =====================================================================
# Why 95.5 - 95.49 != 0.01?
# 1. Hardware uses Base-2 (Binary), not Base-10 (Decimal).
# 2. Decimals like 0.49 become infinite repeating fractions in binary.
# 3. Hardware has a finite grid (53 bits), forcing it to chop/round 
#    the infinite fraction, creating microscopic rounding errors.
# =====================================================================

import sys



# --- HARDWARE BOUNDARIES (From sys.float_info) ---

# 1. PRECISION LIMIT (dig=15)
# Floats are only reliable up to 15 decimal digits. 
# Beyond 15 digits, hardware runs out of bits and creates "garbage" values.
print(sys.float_info.dig)  # Output: 15

# 2. THE GRID SIZE (epsilon = 2.22e-16)
# The smallest measurable step the hardware can see above 1.0.
# Any number smaller than this added to 1.0 is completely ignored.
print(sys.float_info.epsilon)  # Output: 2.220446049250313e-16

# 3. THE CEILING (max = 1.79e+308)
# The absolute largest number a float can hold before overflowing to 'inf'.
print(sys.float_info.max)  # Output: 1.7976931348623157e+308


# --- VETERAN SOLUTIONS ---

# Option A: For display issues, use f-string formatting to round.
print(f"{95.5 - 95.49:.2f}")  # Output: '0.01'

# Option B: For math accuracy (Finance/Safety), use strings with Decimal.
from decimal import Decimal
print(Decimal('95.5') - Decimal('95.49'))  # Output: 0.01 (Exact)

print(f'This is complete information {sys.float_info}')

'''
sys (System) is about Python's internal runtime environment and its immediate interaction with the CPU/Memory (e.g., arguments, limits, paths, exits).

os (Operating System) is about manipulating the external environment (e.g., creating files, deleting directories, checking environment variables).

'''