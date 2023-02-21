

def get_valid_ing(prompt: str) -> int:
    """

    Args:
        prompt:

    Returns:

    """
    return int(get_valid_float(prompt))


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
        "Invalid number. Please enter a valid number."
        return get_valid_float(prompt)
    return value
