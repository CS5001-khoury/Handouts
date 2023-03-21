# Module 10 Activity - Classes, Objects == Encapsulation

Take a moment and list all `types` that come to mind. We have covered a fair number of them, though we may not think of them as `types`. 


Here are a few to help you:
* int - an integer
* float - a floating point number
* str (string) - an immutable sequence of characters
* tuple - an immutable sequence of objects
* list - a mutable sequence of objects
* set - an unordered collection of unique objects
* dict (dictionary) - a mutable mapping of keys to values


Technically, with those types it would be possible to write most programs. However, it would be a lot of work. We can make our lives easier by creating our own `types`. We can do this by creating our own `classes`. A `class` is a blueprint for creating objects. An `object` is an instance of a class. 

Another way to put it, we get to make our own legos! We then use these legos to build our programs.

## Creating a Class

`class` is a keyword in Python. It is used to define a new class. The syntax is as follows:

```python
    class ClassName:
        # class body
```
Anything that is indented under that class "belongs" to that class/object.

> A note on class/object  
> The terms are interchangeable in python. For some people, it helps to think of the class as a blueprint, but once the value is created in memory, it is an object. The more you deal with memory structures, the more it helps to have different terms, but for now treat them as interchangeable.


## Creating an Object

To create an object, we call the class name as if it were a function. This is called `instantiation`. The syntax is as follows:

```python
    object_name = ClassName()
```

For example, if we have a class called `Movie`, and we have a number of items that belong to that movie, including name, list of actors, rating, year released, etc. We can create a class to represent that movie. We can then create an object for each movie we want to track. 

```python
    class Movie:
        def __init__(self, name: str, cast: list, rating: int, year: int):
            self.name = name
            self.cast = cast.copy() # discussion, if this is a list, why would I want to copy this?
            self.rating = rating
            self.year = year
```

> Discussion Topic:  
> Assuming `cast` is a list, why would we want to copy it? Technically we didn't have to do that, but take a moment to draw the memory structure, is a copy "safer" in this case? Why or why not?


### Industry Practices 

It is common to protect your data in industry, especially if you want to 'hide' certain values. In the above example, let's say we only wanted to allow the user to change the rating. We can do this by making the other values private. We do this by adding a double underscore `__` before the name of the variable. 

```python
    class Movie:
        def __init__(self, name: str, cast: list, rating: int, year: int):
            self.__name = name
            self.__cast = cast.copy()
            self.__rating = rating
            self.__year = year
```

Now, if we try to access the values, we get an error. 

```python
    >>> movie = Movie("The Matrix", ["Keanu Reeves", "Laurence Fishburne"], 5, 1999)
    >>> movie.__name
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Movie' object has no attribute '__name'
```

We can still access the values, but we have to use a special function to do so. This is called a `getter`. We can create a getter by using the `@property` decorator. 

```python
    class Movie:
        def __init__(self, name: str, cast: list, rating: int, year: int):
            self.__name = name
            self.__cast = cast.copy() 
            self.rating = rating
            self.__year = year

        @property
        def name(self):
            return self.__name  #notice, every function uses (self) as the first parameter

        @property
        def cast(self):
            return self.__cast # we can access the variables set in __init__ by using self.__variable_name


        @property
        def year(self):
            return self.__year
```

By using the `@property` decorator, we can now access the values. 

```python
    >>> movie = Movie("The Matrix", ["Keanu Reeves", "Laurence Fishburne"], 5, 1999)
    >>> movie.name
    'The Matrix'
    >>> movie.cast
    ['Keanu Reeves', 'Laurence Fishburne']
    >>> movie.year
    1999
```

But we can't write to the values.  Trying the following would produce an error:
    
```python
    >>> movie.name = "The Matrix Reloaded"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
```

However, since rating is not private, we can still write to it. 

```python
    >>> movie.rating = 4
    >>> movie.rating
    4
```

It  is also common (especially in other languages), to create two functions for every attribute, a `get` and a `set`. In python, we can do this by using the `@property` decorator, and then `@variable_name.setter` decorator. This is more advanced than this course, but it is worth exploring on your own. The [code.py](code.py) file has an example of this, and why it is useful as we can control some conditions before the value is changed. 

## Methods
Objects have methods, which are functions the "belong" to that object. It means these functions can use the information stored inside of the object, since the `self` parameter is a requirement for a method. 

You have seen this for string, with methods like `upper()`, `lower()`, `split()`, etc. 

```python
    >>> "hello".upper()
    'HELLO'
    >>> "hello".lower()
    'hello'
    >>> "hello".split()
    ['hello']
```

We can create our own methods. 

```python
   def has_actor(self, actor: str) -> str:
        for actors in self.__cast:
            if actor.lower() in actors.lower():
               return actors  # why did we do it this way, instead of just return actor in self.__cast
        return ''
```

> Discussion Topic:  
> We could have just returned `actor in self.__cast`. Why did we do it this way? What are the pros and cons of the approach
> used above. You may want to test out the code, and come up with how they are different. 


## Built-in Methods
There are a number of methods built into python classes, that are used to make your life easier. A few of them are

* `__str__` - this is used to return a string representation of the object. The goals is to make it readable (ideally for printing)
* `__eq__` - this is used to compare two objects. It is used when you use the `==` operator.
* `__lt__` - this is used to compare two objects. It is used when you use the `<` operator.
* `__gt__` - this is used to compare two objects. It is used when you use the `>` operator.
* `__le__` - this is used to compare two objects. It is used when you use the `<=` operator.
* `__ge__` - this is used to compare two objects. It is used when you use the `>=` operator.
* `__ne__` - this is used to compare two objects. It is used when you use the `!=` operator.
* There are a number of others all connected to operators (+, -, *, /, etc). Obviously, this doesn't make sense for all objects, but some it does!
* For almost all classes, it is suggested you implement `__str__` and `__eq__`. (and eventually `__hash__`, once you explore hashing more in the future!)

```python

def __convert_rating(self, val: int, min_s : int =0, max_s: int =5) -> str:
    val = int(val) 
    if val < min_s:
        val = min_s
    if val > max_s:
        val = max_s
    return "*" * val

def __str__(self) -> str:
    return f"{self.__convert_rating(self.rating):<{7}}{self.name}"
```

Then we can do the following:

```python
    >>> movie = Movie("The Matrix", ["Keanu Reeves", "Laurence Fishburne"], 5, 1999)
    >>> print(movie)
    *****  The Matrix
```

**TASK** Look review the code in the [code.py](code.py) file. Discuss how it can be used in star_rating_app.py. What are the pros and cons of using it? What functions would you have to change? 

## Encapsulation

In Object Oriented Programming (OOP), you have four main concepts: Abstraction, Encapsulation, Inheritance, and Polymorphism. We have already discussed Abstraction, and we will discuss Inheritance and Polymorphism in 5004. Encapsulation is the concept of hiding the implementation details of an object. Or another way to look at it, you assume your block works, so you don't need to know the details of how it works. 

Whenever you work with objects, you try to set them up so they are a single set of related ideas! The "atom" of that idea if you will. You can then build these different blocks together to make a program. Often, you determine what needs to be objects using the same design process you use for functions, but instead you think about the components you need for you program. 

Then for each component, you think about what attributes and methods it needs for that idea to be "complete". For this reason, OOP is the main paradigm used in industry, as it allows team members to focus building very specific objects, while other people assemble those objects into working programs. 

> Discussion Topic:  
> In your own words, describe encapsulation, and discuss with the Movie object which would be good function to exist in movie or not. The "answer" is less than you think, as ideally Movie should only have the methods and attributes that are needed to represent a movie, and other code deals with parsing the file or input from the client. This allows you to use the movie object across programs in different ways!


## Finally

As a group, work on a couple coding practices. Make sure to copy the code into python tutor to discuss the results/see the memory. What happens when an object is passed as a parameter, and then you modify it inside that function?  