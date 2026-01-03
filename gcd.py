def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Return the absolute value to handle negative inputs

# Example usage:
print(gcd(48, 18))  # Output: 6
print(gcd(54, 24))  # Output: 6
