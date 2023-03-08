""" 
Sample code for Module 9 handout.

"""
from typing import List, Dict
import sys

# While we are using globals, this is a bad example of using them,
# as we are using them to store data that is not constant.

CODES = {
    "UA": "United Air Lines",
    "AA": "American Airlines",
    "DL": "Delta Airlines",
    "AS": "Alaska Airlines",
    "HA": "Hawaiian Airlines",
    "WN": "Southwest Airlines",
    "NK": "Spirit Airlines",
    "B6": "JetBlue Airways",
    "F9": "Frontier Airlines",
    "VX": "Virgin America",
    "US": "US Airways",
}


FLIGHTS = [
    "AA2336",
    "US840",
    "AA245",
    "UA940",
    "DL2398",
    "AS120",
    "HA15",
    "WN727",
    "NK4",
    "B6JFK",
    "F9ORD",
    "VXSEA",
    "G4LAS",
]


WORDS = [
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana",
    "apple",
    "pear",
    "orange",
    "apple",
    "kiwi",
    "apple",
    "banana",
]


def count_words(words: List[str]) -> Dict[str, int]:
    """Count the number of times each word appears in a list.

    Examples:
    >>> count_words(["apple", "orange", "apple", "pear", "orange", "banana"])
        {'apple': 3, 'orange': 2, 'pear': 1, 'banana': 1}
    >>> count_words(["apple", "apple", "apple"])
        {'apple': 3}

    Args:
        words(List[str]): A list of words.

    Returns:
        A dictionary of word counts.
    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def list_airlines_from_flights(flights: List[str], codes: Dict[str, str]) -> List[str]:
    """Return a list of airlines from a list of flight codes.

    Examples:
    >>> list_airlines_from_flights(["AA2336", "US840", "AA245"], CODES)
        ['American Airlines', 'US Airways', 'American Airlines']
    >>> list_airlines_from_flights(["AA22", "NK40", "HA245"], CODES)
        ['American Airlines', 'Spirit Airlines', 'Hawaiian Airlines']

    Args:
        flights(List[str]): A list of flight codes.
        codes(Dict[str, str]): A dictionary of airline codes and names.

    Returns:
        A list of airline names.
    """
    airlines = []
    for flight in flights:
        airline_code = flight[:2]
        try:
            airline = codes[airline_code]
            airlines.append(airline)
        except (
            KeyError
        ):  ## this is a common try / except block with dictionaries, especially if you are unsure about all keys being there
            print(
                f"Invalid airline code: {airline_code} for flight {flight}.",
                file=sys.stderr,
            )
    return airlines


def main() -> None:
    """Main function."""
    print(list_airlines_from_flights(FLIGHTS, CODES))
    print(count_words(WORDS))


if __name__ == "__main__":
    main()
