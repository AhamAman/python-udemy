''' Chapter 5: Floating Point Numbers'''

import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")

#see how interpretor treats the floating point numbers
print(sys.float_info)