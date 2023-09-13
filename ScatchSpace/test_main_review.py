""" 
Tests the MainReview.py example.
"""

import MainReview

def test_get_lotto_numbers():
    if MainReview.get_lotto_numbers() == "10,12,13,14":
        print("Test passed")
    else:
        print("Test failed")


def main():
    test_get_lotto_numbers()

if __name__ == "__main__":
    main()