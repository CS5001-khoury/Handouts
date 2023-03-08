# Module 09: Dictionaries and Sets

For this learning activity, we will explore dictionaries and methods related to them. 


## Review of Sets
As a quick review of sets, 

* A set is a list made up of unique only elements. It is also unordered, meaning python *may* change the order of the elements
from the ordered you entered it.


Like a list, you can declare a set directly, or you can use the `set()` function.  You should open your
python interpreter and try out the following commands:

```python
s = {1, 2, 2, 3, 4}
print(s)

sl = set([1, 2, 2, 3, 4])
print(sl)
```

If  you should see the following output:

```text
{1, 2, 3, 4}
{1, 2, 3, 4}
```

* Notice the elements are unique. 
* They are mutable using `add` and `remove` methods.

You will also find that for python you can't add a list or tuple to a set, but you can add a string or a number. 


## Dictionaries

Dictionary is a data structure that is similar to a list, but instead of using an index, you use a key. 

Dictionaries are:  
* Mutable
* Keys are Unique
* Key:Value pairs are used to access the data

> Discussion Item:  
> What are some cases you can think of that having a key,value pair would be useful as compared to using list indexes?

### Deeper Thinking of Use Cases
Now thinking a bit deeper, why would we *NOT* use a dictionary for a movie -> rating pair? Discuss. If it helps, IMDB lists over 1 million movies made in the US alone (32 million shows world wide). However, looking at unique movie names there are only a little over 950,000.

In practice, they keep a structure of a unique id (UID), that pairs with a grouping of movie name, rating, and other data they have associated with it. They then have additional structures that can quickly look up names, and return a list of items based on those names. Once someone narrows down which movie, they can pull the rating and other information based on the UID. If your head hurts thinking about it, don't worry! You will continue to explore how this would work in future classes.  

### Declaring a Dictionary

Dictionaries can be declared directly, or elements can be added using short notation. 

```python
d = {"UA": "United Air Lines", "AA": "American Airlines", "DL": "Delta Airlines", "AS": "Alaska Airlines", "HA": "Hawaiian Airlines", "WN": "Southwest Airlines", "NK": "Spirit Airlines", "B6": "JetBlue Airways", "F9": "Frontier Airlines",  "VX": "Virgin America"}

print(d) # would print as it was entered. Try it out!
# {'UA': 'United Air Lines', 'AA': 'American Airlines', 'DL': 'Delta Airlines', 'AS': 'Alaska Airlines', 'HA': 'Hawaiian Airlines', 'WN': 'Southwest Airlines', 'NK': 'Spirit Airlines', 'B6': 'JetBlue Airways', 'F9': 'Frontier Airlines', 'VX': 'Virgin America'}
```

You can also add elements to a dictionary using the following syntax:

```python
d["G4"] = "Allegiant Air"
print(d)
```

Now, let's say you have a list of flight numbers, you can use the dictionary for *quick* lookup of the airline name. Based on the flight number combination.

```python
flights =  ['AA2336', 'US840', 'AA245', 'UA940', 'DL2398', 'AS120', 'HA15', 'WN727', 'NK4', 'B6JFK', 'F9ORD', 'VXSEA', 'G4LAS']
```

## TASK: Practice
As a group, write a program that will take the list of flights and print out the airline name associated with each flight! 

Notice that the airline code is the first two characters of the flight number, so you can use string splicing to help you get the unique identifier of the airline.

## Replacing a Value
You can also replace a value of a dictionary using direct access.

```pthon
d["UA"] = "United Airlines"
```

### Thinking Deeper - what can be keys?
You can use any immutable object as a key.  This means you can use a string, number, or tuple.  You can't use a list or dictionary as a key.  Why do you think this is?  Discuss with your group.

Furthermore, you will get `TypeError: unhashable type: 'list'` if you try to use a list as a key. Hashable means that the object can be converted to a mostly unique number for indexing.  This is a bit of a deep topic, but we will explore it in a future class (CS 5008). Sufficient to know now, when you hear the term "hashmap" or "hashtable" a dictionary in python is a hashmap. 

## Useful Dictionary Methods

There are a number of useful dictionary methods. You can find a full list of them looking at the python [documentation for dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

For our use, let's explore ways we can iterate over a dictionary, and also combine lists into dictionaries. 

### Iterating over a Dictionary
You can iterate over a dictionary using a `for` loop.  You can iterate over the keys, values, or key,value pairs. 

```python
for key in d:
    print(key)
```
Try it out!

```python
for key in d:
    print(d[key])
```

Try it out, what is the difference between the two prints? Now, lets try to get a key and value at the same time!

```python
for key, value in d.items():
    print(key, value)
```

Notice the `.items()` method.  This is a method that is available on dictionaries.  It returns a list of tuples, where each tuple is a key,value pair.  You can also use the `.keys()` and `.values()` methods to get a tuple of keys or values. By using "unpacking" we can quickly turn that .items() tuple into two variables, key and value (note, these are variable names so technically, you don't need to use these names, but it is a good convention to use).

### Combining Lists into Dictionaries
You can also combine two lists into a dictionary.  This is useful if you have a list of keys, and a list of values.  You can use the `zip()` function to combine the two lists into a list of tuples.  Then you can use the `dict()` function to convert that list of tuples into a dictionary. 

```python
keys = ['a', 'b', 'c', 'd', 'e']    
values = [1, 2, 3, 4, 5]
d = dict(zip(keys, values))
print(d)
```
Try it out!  What do you think the output will be?  What happens if the lists are not the same length?  Discuss with your group.


## TASK: Practice

Let's now also think about the using dictionary to count entries. Assume we have the following list of words:

```python
words = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'apple', 'pear', 'orange', 'apple', 'kiwi', 'apple', 'banana']
```
We can loop through the list, anytime we find a new word, we can add it to the dictionary, and set the value to 1.  If we find the word again, we can increment the value by 1.  This is a common pattern for counting things.  Let's try it out!

As a group, follow the algorithm and build a dictionary that counts the words. The final dictionary should look like (if using the same list).

```python
{'apple': 5, 'orange': 3, 'pear': 2, 'banana': 2, 'kiwi': 1}
```


### Coding Practice
Finally, with your group select at least two of the modules coding practice problems. I encourage you to solve them together, and also use [Python Tutor](https://pythontutor.com/python-debugger.html) to view the memory structure of your solution! 