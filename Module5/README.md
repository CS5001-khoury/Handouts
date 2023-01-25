# Workshop 05 - Understanding Sequential Data

For this workshop, we will first play a game and then visualize the memory structure being sequential data.

> **Sequential Data**  
> In python Lists, Tuples, Strings, Sets are ordered sequential data, meaning they are hold multiple pieces of information
> together in an ordered sequence. For Strings it is a bunch of single characters together. For Lists it is any type in a mutable manner, for tuples it is any type in an immutable manner, and for sets it is unique value of types in an immutable manner. 

## Wheel of Fortune / Hang'um

Wheel of Fortune and Hangman share a similar premise. You are guessing a word or phrase, based on guessing letters. 

As a group, have one person be the 'host' and others take turns guessing letters in the phrase the host decides. As the host 
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

Q4 - What is better if you want to have the names be variable length?


## Pattern Matching
Often when we look at data, we are looking at patterns. We will explore this concept more with file formats, but let's think about strings.


Given the following strings

```python
neu_boston = "Boston,42.3395683,-71.0922272"
neu_sanfran = "San Francisco,37.79292,-122.4068792"
neu_vancouver = "Vancouver,49.2806832,-123.1178707"
```

Can you see a pattern? 

> PLACE,LATITUDE,LONGITUDE 

Write a 2 functions. One that reads in a string with that pattern, and returns the location name. The second function reads in that string and returns a tuple of Latitude and Longitude.

Later when we deal with files, you could load a file with 100 such strings, but your functions would still work. They care more about the pattern, than the values themselves!

If you look at [code.py](code.py), you will see an example that uses a while loop instead of three variables. Discuss the code. 


### Further Thinking
Most file formats are patterns that follow a specific format! HTML parsing involves looking for the HTML tags 

```html
<h1>heading</h1>
<p>This is a paragraph about heading</p>
```

And seeing the pattern formed by the tags and information. 



## Visualizing Data

It is important to visualize your code. [Python Tutor] is a tool that can help with that!  

* View the [visualization for code.py]. Hint right click to open in a new tab. 

* As a group, work on a couple problems from your module coding practice. Use the Python Tutor to visualize the code flow of your mini programs. 








[Python Tutor]: https://pythontutor.com/python-debugger.html#mode=edit
[visualization for code.py]: https://pythontutor.com/visualize.html#code=def%20string_games%28name%20%3D%20%22Guido%20van%20Rossum%22%29%3A%0A%20%20%20%20length%20%3D%20len%28name%29%0A%20%20%20%20print%28f%22Q1%3A%20%7Blength%7D%22%29%0A%0A%20%20%20%20first%20%20%3D%20name%5B%3A5%5D%0A%20%20%20%20length%20%3D%20len%28first%29%0A%20%20%20%20print%28%28first,%20length%29%29%0A%0A%20%20%20%20first%20%3D%20name%5B%3Aname.find%28'%20'%29%5D%0A%20%20%20%20print%28%28first,%20len%28first%29%29%29%0A%0A%0Adef%20get_area_name%28data%29%3A%0A%20%20%20%20return%20data.split%28','%29%5B0%5D%0A%0A%0Adef%20get_lat_long%28data%29%3A%0A%20%20%20%20vals%20%3D%20data.split%28%22,%22%29%0A%20%20%20%20lat%20%3D%20float%28vals%5B1%5D%29%0A%20%20%20%20lon%20%3D%20float%28vals%5B2%5D%29%0A%20%20%20%20return%20lat,%20lon%20%20%23multiple%20return%20values%20become%20a%20tuple%20by%20default%0A%0Adef%20show_pattern%28%29%3A%0A%20%20%20%20locations%20%3D%20%28%22Boston,42.3395683,-71.0922272%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22San%20Francisco,37.79292,-122.4068792%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Vancouver,49.2806832,-123.1178707%22%29%0A%0A%20%20%20%20counter%20%3D%200%0A%20%20%20%20while%28counter%20%3C%20len%28locations%29%29%3A%0A%20%20%20%20%20%20%20%20name%20%3D%20get_area_name%28locations%5Bcounter%5D%29%0A%20%20%20%20%20%20%20%20coords%20%3D%20get_lat_long%28locations%5Bcounter%5D%29%0A%20%20%20%20%20%20%20%20print%28f%22%7Bname%7D%20can%20be%20found%20at%20coordinates%3A%20%7Bcoords%7D%22%29%0A%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%0Adef%20main%28%29%3A%0A%20%20%20%20string_games%28%29%20%23%20defaults%20to%20%22Guido%20van%20Rossum%22%0A%20%20%20%20print%28%22%23%23%23%23%23%20What%20happens%20when%20we%20put%20in%20a%20different%20name%3F%20%23%23%23%23%23%22%29%0A%20%20%20%20string_games%28%22Barbara%20Liskov%22%29%20%20%0A%20%20%20%20%23%23%20why%20did%20find%20work,%20but%20just%20using%20the%20location%20didn't%3F%0A%0A%20%20%20%20print%28%22%23%23%23%20looking%20at%20patterns%20%23%23%23%22%29%0A%20%20%20%20show_pattern%28%29%0A%0A%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29&cumulative=false&curInstr=73&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false