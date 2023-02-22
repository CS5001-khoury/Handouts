"""
Example of loading a file into a tuple, and tests to help look at it.
"""


def load_file(file_name: str) -> tuple:
    """
     Loads a file of numbers into a tuple

    Args:
        file_name: name of (text) file to open

    Returns:
        a tuple of numbers, ignores any line that isn't a number

    """
    values = []  # set up an empty list to return, even if the file is not found
    try:
        with open(file_name) as file:  # read is default and can be left off
            for line in file:
                try:
                    values.append(float(line.strip()))
                except ValueError:
                    pass  # skip that line, maybe good to print an error, but decided not to this time
    except FileNotFoundError:
        print(f"{file_name} not found!")
    except IOError as io:
        print(io)
    return tuple(values)


def average(values: tuple) -> float:
    return sum(values)/len(values)


def tester(file):
    contents = load_file(file)
    if contents:
        print(contents)
        print(f"Average: {average(contents)}")


def main():
    print("### TEST 1 ###")
    tester("test1.txt")
    print("### TEST 2 ###")
    tester("test2.txt")
    print("### TEST 3 ###")
    tester("test_invalid_lines.txt")
    print("### TEST 4 ###")
    tester("file_not_found.txt")


if __name__ == "__main__":
    main()
