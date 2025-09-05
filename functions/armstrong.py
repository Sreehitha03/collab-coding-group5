def is_armstrong(num: int) -> bool:
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its digits
    each raised to the power of the number of digits.

    Example: 153 -> 1^3 + 5^3 + 3^3 = 153

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is Armstrong, False otherwise.

    Author: Keshav Kabra
    """
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num
