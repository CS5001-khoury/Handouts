# good test cases
# sets / tuples
# design activity
# recursion 

def factorial(n: int = 5) -> int:
    """Factorial calculates the mathematical
    factorial, which s N * N-1, or
    5! = 5*4*3*2*1
    4! = 4*3*2*1
    5! = 5 * 4!

    Examples:
        >>> factorial(5)
        120
        >>> factorial(4)
        24
        >>> factorial(0)
        1

    Args:
        n (int): the nth value of factorial

    Returns:
        int: the calculated whole value
    """
    #if n < 0: raise AttributeError("Value > 0")
    val = 1
    for i in range(1, n+1):
        val *=  i
    return val


def test_factorial():
    val_nothing = factorial()
    print('test nothing', val_nothing == 120)
    #val_not_int = factorial(5.5)
    #print('not an int', val_not_int == 120)
    val_neg = factorial(-1)
    print("test neg", val_neg)

def getInput() -> int:
    return int(input("Enter a number: "))


def test_getInput():
    ## entering 5, should return 5
    print("testing 5, ", getInput())


def mem_mutilator(val3)-> list:
    val3 = val3.copy()
    val3[0] = 100
    return val3

def memory_test():
    val1 =[0, 8, 3]
    val2 = [0, 10, 4]
    val2[0] = 5
    val1 = val2
    val1[0] = 2
    val3 = mem_mutilator(val1)
    print(val2)
    print(val3)

grid = ((1, 2, 3),
        (100, 20, 3),
        (100, 200, 300))

def get_col(grid, col) -> tuple:
   lst = []
   for row in grid:
       lst.append(row[col])

   return tuple(lst)  

def get_rows(grid, row_value, loc = 0) ->tuple:
    lst = []
    for row in grid:
        if row[loc] == row_value:
            lst.append(row)
    return tuple(lst)


# ask client to enter a number == n / max
# generate random number 1..n
# ask client for guess
# give feedback for a guess
# keep looping until exit it entered

def guessing_game():
    """
    Asks the client for a number > 0,
    starts the guessing game
    can end if client types exit
    """
    pass 

def play_single_game(correct: int):
    """keeps guessing until correct

    Args:
        correct (int): _description_
    """
    guess = get_guess() 
    results = check_guess(correct, guess)
    print_response(results)
    while(results != 0):
        guess = get_guess() 
        results = check_guess(correct, guess)
        print_response(results)

def get_guess() -> int:
    inp = input("Guess a number: ")
    return int(inp)

def check_guess(correct, guess) -> int:
    """checks correct vs guess, gives if
    high low equal

    Args:
        correct (_type_): _description_
        guess (_type_): _description_
    """
    return correct - guess  

def print_response(difference) ->None:
    if(difference > 0): 
        print("You guessed too low")
    elif difference < 0:
        print("you guessed too high")
    else: 
        print("Correct!")