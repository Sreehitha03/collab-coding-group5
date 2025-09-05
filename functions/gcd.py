"""
Author: Karan Kant
Function: gcd(a, b)
Description: Returns the Greatest Common Divisor (GCD) of two numbers a and b using Euclidean algorithm.
"""

def gcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers")
    return a if b == 0 else gcd(b, a % b)