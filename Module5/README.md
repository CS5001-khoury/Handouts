# Workshop 05 - Understanding Sequential Data

For this workshop, we will first play a game and then visualize the memory structure being sequential data.

> **Sequential Data**  
> In python both Lists, Tuples, Strings, Sets are ordered sequential data, meaning they are hold multiple pieces of information
> together in an ordered sequence. For Strings it is a bunch of single characters together. For Lists it is any type in a mutable manner, for tuples it is any type in an immutable manner, and for sets it is unique value of types in an immutable manner. 

## Wheel of Fortune / Hang'um

Wheel of Fortune and Hangman share a similar premise. You are guessing a word or phrase, based on guessing letters. 

As a group, have one person be the 'host' and others take turn guessing letters in the phrase the host decides. As the host 
you should also include spaces as a character. For example, if my phrase was [Guido van Rossum](https://en.wikipedia.org/wiki/History_of_Python)

I would draw:

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|

which would then match
| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| G | u | i | d | o |   | v | a | n |   | R | o | s | s | u | m |

### Adding Numbers

Now after playing a couple games, you should add numbers to the bottom! However, we are computing scientists, so we start counting at 0.

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

which would then turn into

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| G | u | i | d | o |   | v | a | n |   | R | o | s | s | u | m |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |


> Essentially, you have been thinking of strings as sequential data every time you play these games growing up!

### Try it in python

Let's try it in python. All sequential data shares some similar functions and operations. 


```python
creator = "Guido van Rossum"
length = len(creator)
```
Q1 - what is printed? Discuss and then run the code to see

```python
creator = "Guido van Rossum"
first = creator[:5]
length = len(first)

print((first, length))
```

Q2 - what is printed? Talk about the length, is the 5 "inclusive" or "exclusive" of 5? What is the value before the `:` it is assumed. 

```python
creator = "Guido van Rossum"
first = creator[:creator.find(' ')]
length = len(first)

print((first, length))
```

Q3 - would this print the same thing as the Q2? You may want to look up to see what the find method does!



## Visualizing Data

