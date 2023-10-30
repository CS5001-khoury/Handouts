import time


def fibonacci_iterative(n):
    if n <= 1:
        return n

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]
    


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def time_function(func, *args):
    # Get the start time
    start = time.time()
    # Call the function with the given arguments
    result = func(*args)
    # Get the end time
    end = time.time()
    # Calculate the elapsed time
    elapsed = end - start
    # Return the result and the elapsed time
    return result, elapsed


def main():
    # you may want to increase the numbers some, and try, but be careful on not going too high (50 can take a while)
    print("Fibonacci(10) =", time_function(fibonacci_iterative, 10))
    print("Fibonacci(20) =", time_function(fibonacci_iterative, 20))
    print("Fibonacci(30) =", time_function(fibonacci_iterative, 30))

    print("Fibonacci(10) =", time_function(fibonacci_recursive, 10))
    print("Fibonacci(20) =", time_function(fibonacci_recursive, 20))
    print("Fibonacci(30) =", time_function(fibonacci_recursive, 30))


if __name__ == "__main__":
    main()