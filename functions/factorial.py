"""
Author: Sreehitha
Function: factorial(n)
Description: Returns the factorial of a number n.
"""

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)
