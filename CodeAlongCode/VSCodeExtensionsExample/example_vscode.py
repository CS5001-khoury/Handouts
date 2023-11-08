""" 
This will give stats about grades.
"""
import sys


def line_to_tuple(line: str) -> tuple:
    """
    Converts a line in the format of str,str,str
    to a tuple of float, float, float

    Args:
        line (str): string separated by commas

    Returns:
        tuple: a tuple of floats
    """
    rtn = []
    for val in line.split(","):
        try:
            rtn.append(float(val))
        except ValueError:
            print("Not a float, skipping line", file=sys.stderr)
            return ()
    return tuple(rtn)


def open_file(file_name: str) -> tuple:
    """Opens a file and returns a tuple of tuples
    for each line in the file.

    Args:
        file_name (str): The name of the file

    Returns:
        tuple: a tuple of tuples returning lines
    """
    rtn = []
    with open(file_name) as file:
        is_first = True
        for line in file:
            if is_first:  # skip the first line
                is_first = False
                continue
            val = line_to_tuple(line)
            if val:
                rtn.append(val)
    return tuple(rtn)


def main():
    """
    Asks for a file, and then just prints out 
    the stats for each line.
    """
    file = input("A file please: ")
    try:
        values = open_file(file)
    except FileNotFoundError:
        print("File not found, ending.")
        return
    except IOError:
        print("IO Error, ending")
        return 
    
    ## now do stuff about calculating stats.
    print(values)



if __name__ == "__main__":
    main()

