# Exploring For Loops, Lists, Tuples, Sets

For loops in python go hand in hand with data structures such as lists, tuples, and sets. In this activity, we will explore both the for loop, and dive deeper into sequential data structures. 

## Practice With the For (each/in) Loop

The for loop in python, is often called a for/in or for/each loop in other languages. The idea is:

```text
for (each) item in sequence
```

For this activity, you should work through the examples using your python interactive window. You will also want to have [python tutor] see how the memory is working. 

### For value in a list of values

Assume the following list:

```python
good_guys = ["Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max"]
```

for loops, allow you iterate over the list

```python
for character in good_guys:
    print(character)
```

This is the equivalent to saying

```python
counter = 0
while counter < len(good_guys)
    character = good_guys[counter]
    print(character)
    counter += 1
```

Run both in [python tutor] to see the difference in execution, even though they are equivalent in results. 

### Discussion
* What are some cases to use a for loop?
* What are some cases were a while loop is better (hint: when you don't have a sequence, but there may be other cases that come to mind)?

### Adding Range

Because it is common to run from $0..N$ python has a built in function called `range` that builds a tuple of numbers.

```python
for i in range(0,10):
    print(i)
```

Run the above code, see what happens. Is it inclusive / exclusive of values? You can also run the following to get an idea of what `range` is actually returning

```python
print(range(0,10))
```

> You can also add `step=n` where $n$ is a number, to skip numbers, you should feel free to explore.

Because range exists, we can start blurring the line between while and for loops. Simple counter increments are often best with a for loop. However, there are still cases where `while` shines. For example when you are writing code in star_rating_app, a while makes sense here as we have to check the variable command for the loop condition. 

```python
command, raw = menu()
    movies = []
    while command != "exit":
        if command.find(',') > 0:
            movies.append(add_movie(raw))
        elif command == "add":
            movies.append(add_movie())
        elif command == "list":
            print_movies(movies)
        else:
            print("Invalid command: must be add, list, exit, movie,rating.")
        command, raw = menu()
```
Your code may be different, this is just one way to write the run() function. 

## List, Tuple, Set, String
For loops work best on `sequential data` which is what we current know as 
* string 
* list
* tuple
* set

### Discussion:
* As a group talk about the differences between the four sequential data types. 
* Out of the four listed, which two are **immutable** and which two are **mutable**?

### Sequential Data and Mutability

Why does this term mutability matter for programming? Wouldn't it make sense to just use lists all the time? Often, many programs do just that, and by default many python functions return a list. 

However, when thinking about a **list** a computer not only has to keep memory for the values in the list, it also has to keep extra memory incase that list is expanded. While it depends on the language, it is often double that of what is in the list in worst case!

We can measure that in python by trying the following

```python
from sys import getsizeof
good_guys = ["Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max"]
size_of = getsizeof(good_guys)
print(size_of)
```

While it may vary a bit depending on the system and python version, when running this, the size was 104.

However, happens if we change it to a tuple?

```python
from sys import getsizeof
good_tuple = ("Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max")
size_of = getsizeof(good_tuple)
print(size_of)
```
The memory size dropped to 80. 

Why, because python knows the memory is fixed, so it doesn't have to keep additional information to allow values to be added or removed. Additionally, because the memory is fixed, it can also share memory between objects.

Try the following inside of a file, and then load the file.
```python
good_guys = ["Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max"]
good_guys_copy = ["Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max"]
id(good_guys)
id(good_guys_copy)
```

The `id` function tells you where the object is located in memory. 

while it will change between runs, the output when writing this up was
```
1882969788672
1882965039744
```
two different memory locations. Which makes sense, as they are two different lists that can be modified independently.

Now try the following by putting it into a python file and running it.
```python
good_tuple = ("Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max")
good_tuple_copy = ("Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max")
id(good_tuple)
id(good_tuple_copy)
```

The output when we ran it was
```
2869804528672
2869804528672
```
Yours will vary, and it may even be different depending on how you run the code. However, when you run it as an independent program, python is able to detect that these two variables are pointing to **immutable** items, and thus will just set the variables to the same memory location! This saves overall memory consumption. 

For reference, the memory could be diagramed as the following.

![Memory Model]

However, since strings are immutable, a more detailed representation would be.

![Memory Model Two]


However, that is a bit complicated, so strings just tend to be written as literals.

## Let's dive deeper

Take the following program:

```python
from random import randint

names = ("Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max")

def get_name():
    return names[randint(0, len(names)-1)]


def build_copies(n:int ):
    lst = []
    for val in range(0, n):   
        if (val % 2) == 0:
            lst.append(get_name())
        else:
            lst.append(get_name()+"2")
    return lst


def get_mixed():
    return (["Vizzini", "Rugen", "Humperdinck"], names)
    

def build_complex_structure():
    lst = build_copies(3)
    mixed = get_mixed()
    lst.append(mixed)
    del mixed[0][0] # del removes an item from a list
    print(lst) 


if __name__ == "__main__":
    build_complex_structure()
```

Draw the memory structure of what is going on. For tuples, place them together, and if you have more than one variable pointing towards the tuple, draw those areas to it.   You are free to use [python tutor], but for simplicity it will usually show strings as standard variables not values sitting on the 'heap'. There is a dropdown that will say 'store all objects on the heap', but it can be a bit overwhelming. 

### Discussion

* How many values are being duplicated as compared to using the same location in memory?

* How did the list inside of the tuple get modified? 
  * Hint: it is because it isn't copying, but storing a memory reference to the list. This is a great discussion topic to explore!
  * This is a common error, assuming things are copied all the time. 


## Why does this matter?

For now, the most important part is understanding the vocabulary. However, as you dive deeper into languages, you will find it matters. If things are immutable, it is often easier to work with them in cases of parallel processing and memory management, but they can be expensive if you have to modify them. This is a constant discussion in computers, speed vs. amount of memory to use. Computers can be infinitely fast, if memory was infinite but neither are true.

## Homework Warmup

You will also see in your homework, we used tuples for everything, because your homework causes you to search though lists of lists, but since those lists are never modified - they were better to represent as tuple of tuples. 


For example, to warm you up to your homework

```python
matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))
```

as a group, write a function that takes every nth element from the lists.

For example:

```python
my_func(n):
#...
```
would return `(2, 5, 8)` if $n$ was `1`.  This is the filter_by_column function in your homework. Go ahead and work on it as a group, but please make sure to give credit to the rest of your group members.  Discuss how you can also test this function.  

[python tutor]: https://pythontutor.com/python-debugger.html
[Memory Model]: memory_one.png
[Memory Model Two]: memory_two.png