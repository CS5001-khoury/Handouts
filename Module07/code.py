"""
Module 07 sample code for CS 5001.
"""


def factorial_iterative(n: int) -> int:
    """
    Gives the factorial for any number of
    n using an iterative solution.

    Examples:
        >>> factorial_iterative(1)
        1
        >>> factorial_iterative(4)
        24

    Args:
        n (int): the value to generate

    Returns:
        int: the factorial
    """
    counter = 2
    fact = 1
    while counter <= n:
        fact *= counter
        counter += 1
    return fact


def factorial(n: int) -> int:
    """
    Gives the factorial of any number using
    a recursive solution.

    Examples:
        >>> factorial(1)
        1
        >>> factorial(4)
        24

    Args:
        n (int): the value to generate

    Returns:
        int: the factorial
    """
    if n == 0 or n == 1:
        return 1  # done, exit the function immediately
    return n * factorial(n - 1)


def product(value) -> float:
    """
    Takes in structure of numbers in nested lists. building
    the product of all the numbers across all the lists.

    Examples:
        >>> product((10, 12, (15, 12, (1, 5))))
        108000
        >>> product((10, (12, )))
        120

    Args:
        value: a list of number that can continue equal sublists of numbers

    Returns:
        the product of all numbers in the lists
    """
    if isinstance(value, float) or isinstance(value, int):
        return value  # base case, we have just a single number no list
    if len(value) > 1:
        return product(value[0]) * product(value[1:])
    return product(value[0])


# this main actually doesn't do anything other than run the doctest when the file is loaded
# this is another way to run them if you don't run it via the command line
# only makes sense if the file only has support functions and not a full program starting
# with main
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
