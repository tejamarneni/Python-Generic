def greet(name: str) -> str:
    """
    Returns a personalized greeting.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting message.

    Raises:
        TypeError: If name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello, {name}!"


def sum_numbers(*numbers: int) -> int:
    """
    Returns the sum of multiple integers.

    Args:
        *numbers (int): Variable number of integers.

    Returns:
        int: The sum of all numbers.

    Example:
        >>> sum_numbers(4, 5, 6)
        15
    """
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All inputs must be integers")
    return sum(numbers)
