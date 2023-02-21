import sys


def get_valid_int(prompt: str) -> int:
    """

    Args:
        prompt:

    Returns:

    """
    return int(get_valid_float(prompt))  # a float can always be converted to an int


def get_valid_float(prompt: str) -> float:
    """

    Args:
        prompt (str):

    Returns (float):

    """
    try:
        s_value = input(prompt).strip()
        value = float(s_value)
    except ValueError:
        print("Invalid number. Please enter a valid number.", file=sys.stderr)
        return get_valid_float(prompt)
    return value
