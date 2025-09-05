"""

Author: Ketan Sharma
Function: fibonacci(n)
Description: Returns the nth fibonacci number of series.

"""
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
