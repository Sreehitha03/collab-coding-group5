"""
Prime Number Checker
Author: K. Bhargav
"""

def is_prime(n: int) -> bool:
    """
    Check whether a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check for factors up to square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
