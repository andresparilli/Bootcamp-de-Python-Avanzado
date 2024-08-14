def sum(*args):
    """
    Sums an indefinite number of integers.

    Args:
        *args: Variable arguments representing the numbers to be summed.

    Returns:
        The sum of all the provided integers.

    Raises:
        TypeError: If any of the arguments is not an integer.

    >>> sum(2, 3)
    5
    >>> sum(10, -3, 5)
    12
    >>> sum()  # No arguments
    0
    >>> sum(2, 3.5)  # Non-integer argument
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 11, in sum
    TypeError: All arguments must be integers.
    """

    # Verify that all arguments are integers
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("All arguments must be integers.")

    # Sum all the arguments
    total = 0
    for num in args:
        total += num
    return total

# Usage examples
print(sum(2, 3))        # Output: 5
print(sum(1, 5, 7, 2))  # Output: 15
print(sum(2, 3, 4, 10))  # Output: 19
