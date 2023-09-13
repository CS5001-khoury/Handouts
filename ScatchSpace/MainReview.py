"""
Example of python entry points.
"""

def get_lotto_numbers():
    return "10,12,13,14"

def hello():
    print("hello world")

def goodbye():
    print("Thank you for playing the lotto")

def main() -> None:
    print("In main")
    hello()
    goodbye()


if __name__ == "__main__":
    main()
