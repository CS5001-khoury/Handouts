# Module 07 Activity - Recursion 

Recursion is at the heart of **divide**, **conquer**, and **glue**. Why? Because many problems can often be broken up 
into simple cases, and then solving that simple case builds the solution to more complex cases. 

The problem is people often overcomplicate their point of view, and the solution is to try to force yourself to
think into the simplest terms.  

In this activity, we will cover some base examples of recursion, and then explore more complex examples to help
get a better understanding of why recursion.  Recursion is a topic you will continue to come across when working
within computer science, so don't worry if it takes a bit to understand! As a reminder, if you are
struggling you are learning. 


## Factorial
One of the  most common recursive "entry" problem is factorial. A factorial is the product of
integers with all integers smaller than it until 1.

$$5! = 5 * 4 * 3 * 2 * 1$$

However, $5!$ can also be represented as

$$5! = 5 * 4!$$

and $4!$ can be 

$$ 4! = 4 * 3! $$

This means you start to see a **pattern** in the problem. It is 

$$n * (n-1)! $$  

Until $n=1$ which then it just is 1 for the answer!

## Coding Factorial?

We can code a `while` loop for factorial using a counter. 

```python
def factorial_iterative(n: int) -> int:
    counter = 2
    factorial = 1
    while counter <= n:
        factorial *= counter 
        counter += 1
    return factorial 
```

### Task: Write and Document
> **TASK**  
> Write out factorial in a file. Make sure to include a full docstring including examples of input/output. Then
> write test function to test factorial. Question: Did writing a full docstring with examples help you determine the 
> tests to consider? 

#### Advanced  Feature / Discussion 
When you write a docstring with tests, the format is often what you would see if you ran the function in python 
directly. For example:

```python
def factorial_iterative(n: int) -> int:
    """
    description
    
    Examples:
        >>> factorial_iterative(1)
        1
        >>> factorial_iterative(4)
        24
        
    Args:
        n (int): description 
         
    Returns:
        int: describe what is returned
    """
```
 
If you use the above format, this is a command line program you can run that will run the tests in the documentation.

```terminal 
> python -m doctest -v filename.py
```

While using [doctest] isn't required, for *pure* functions (no printing, input, or variable mutation), it saves
time testing as you don't have to write the tests if they are documented in docstrings and doctests is run!

## Coding Factorial Recursively 

Recursive functions have **at least two** parts always.  

### Part 1 - Base Case
The first thing you think about with a recursive function is the base or simplest case. For factorial, that is "1" 
or arguably 1 or 0 as $0!$ is defined to be 1. 

You always write the base case first!

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # done, exit the function immediately 
```

If I run the above, it works for factorial 0 or factorial 1.

### Part 2 - Recursive Condition

The next part is you consider your recursive condition. Above we defined it as:

$$n! = n * (n-1)!$$

converting that to code we would get

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # done, exit the function immediately 
    return n * factorial(n-1)
```

When we run this function, we can "draw it out" by doing the following

```mermaid
flowchart LR
    start --> factorial_4("factorial(4)")
    factorial_4 --> factorial_3("factorial(3)")
    factorial_3 --> factorial_2("factorial(2)")
    factorial_2 --> factorial_1("factorial(1)")
    factorial_1 -- " 1 " --> factorial_2
    factorial_2 -- " 2 " --> factorial_3
    factorial_3 -- " 6 " --> factorial_4
    factorial_4 -- " 24 " --> returns("end")
```

Note: start and end are often not included when sketching out function calls like this

### TASK: Visualize it
As a group use [python tutor] to run the recursive function, and see the function stack and how it builds. Run it
with a variety of input, and then try to "draw out" the results on your own. 


## Why Recursion - Deep Dive?

The most common struggle students have learning recursion is the "why". We just showed it can be done with a loop
why do we need to use recursion? However, let's say we wanted to take the product of all values in a list.

```python
def product_values_list(values) -> float:
    rtn = 1.0 
    for i in values:
        rtn *= i 
    return rtn

test = (10, 2.2, 23, 5, 15)
sol = product_values_list(test)
print(sol)
```
Ok... But what if we wanted to add the ability to have more lists or single values in the list?

```python
test = (10, ((1, 2), 4, (13, 2), 10))
```
Seems weird but depending on where you are getting the data, that is possible. 

### Discuss? 
Can you still use a loop to access all the values? If you use `type()` or [`isinstance()`](https://www.w3schools.com/python/ref_func_isinstance.asp) 
it may be possible, but you would have to know exactly how many nested lists. 

Let's make it harder. Let's say you have list of lists, and you don't know how many you will have. Something like the 
following!

```python
test = (10, (1, (2, 4, (13, 2)), 10))
```
> If your head is hurting, that is alright!

The above structure is impossible to do with loops, as the number of nested lists is infinite. However, recursively,
it is possible, as recursion looks at the simple case and builds up. 

```python
def product(value) -> float:
    if isinstance(value, float) or isinstance(value, int):
        return value  # base case, we have just a single number no list
    if len(value) > 1:
        return product(value[0]) * product(value[1:])
    return product(value[0])
```
The above code can be challenging. We encourage you to run it in [python tutor] to get a better understanding, but
you do not have to fully understand. You will cover what is known as "recursive data structures" in a later class!


## Practice
Work through multiple problems in Coding Practice 07. Make sure to run them in [python tutor] to better
understand your solutions! 



[doctest]: https://docs.python.org/3/library/doctest.html
[python tutor]: https://pythontutor.com/python-debugger.html