"""
Author: Harsh
Function: reverse_number(n)
Description: Returns the reverse of the given integer n.
"""

def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1   # Handle negative numbers
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

