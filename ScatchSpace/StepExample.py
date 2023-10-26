# this is an example of using step with slice


def reverse(string: str) -> str:
    """Reverses a string using string splice and step

    Examples:
        >>> reverse("hello")
        'olleh'
        >>> reverse("olleh")
        'hello'
    """
    return string[::-1]  # step is -1


def reverse_every_other(string: str) -> str:
    """Reverses every other character in a string

    Examples:
        (starts at o, then l, then h)
        >>> reverse_every_other("hello")
        'olh'

        >>> reverse_every_other("racecar")
        'rccr'

    """
    return string[::-2]  # step is -2


def slice(item: list | tuple | str, start: int = 0, 
          end: int | None = None, step: int = 1) -> list | tuple | str:
    """Example of slice if written out as its own function.

    This example takes into account negative number conversion
    and starts from the end of the item if the values are negative.

    Purposely written so each step is highlighted, even though
    there may be some better ways to do it with less lines. 


    examples:
        >>> slice("hello", 1, 4, 1)
        'ell'
        >>> slice("hello", 1, 4, -1)
        'lle'
        >>> slice("hello", -1, -4, -1)
        'oll'

    """
    if end is None:
        end = len(item)  # set the length of end to the length of the item by default

    if start < 0:
        start = len(item) + start
    if end < 0:
        end = len(item) + end
    result = []
    if step > 0:
        i = start
        while i < end:
            result.append(item[i])
            i += step
    elif step < 0:
        i = start
        while i > end:
            result.append(item[i])
            i += step
    if isinstance(item, str):
        return "".join(result)
    elif isinstance(item, tuple):
        return tuple(result)
    return result
