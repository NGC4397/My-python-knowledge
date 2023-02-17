"""In this section, I offer a quick walkthrough of useful commands worth knowing
for a programmer."""

"""First in the queue is the "input" function. It accepts incoming values 
from the user. Often, when receiving data, it is convenient to immediately 
convert them into the desired format. To do this, we need to put the input 
function inside the brackets of a variable, for example, in int(), float(), 
str(), and others. Interestingly, if we put the result of input inside list(),
 our output will be an array, with the components of the input value listed 
 in commas. This is useful if we need to handle each part of the data separately. 

In addition you can put the text that will greet the user into input() 
right away. Let's see some examples:"""

# print(list(input()))
# print(int(input("Enter the number: ")))



"""Next in line is the "append" function. It adds a new value to the end 
of the "list". If we want to add a value by a certain index, then we should
use the function "insert", and if we want to remove a certain value, then 
the function "pop" (If we want to remove the first matching value,
we should use the "remove" function). And to find the index of a particular value, 
the function "index" comes in handy. For sorting, we can use "sort"."""

stars = ["Sun", "Alpha Centauri", "Stephenson 2-18"]
stars.append("WOH G64")
stars.insert(0, "GCIRS 7")
stars.pop(1)
stars.sort()
print(stars, "\n", "GCIRS 7 position: ", stars.index("GCIRS 7")+1, "\n")

"""If we want to divide a number by another number and get two values as
 an integer result of division and its remainder, the function "divmod" 
 comes in handy."""

print("The result of division and the remainder are equal: ", divmod(21, 8), "\n")



"""If we want to count the number of certain elements in a string, the 
function "count" will help us. In general, there is a whole library 
for handling strings (which we will probably discuss in the future) 
called "Regular expression". For now, however, we will limit ourselves 
to the function "count". Let's count and print the number of letters 
"a" in one of the most famous star systems. """

star_system = "Alpha Centauri"
print("'a' in Alpha Centauri: ", star_system.count("a"), "\n")

"""You may have noticed that the "count" function did not count all 
the letters "a". This happened because this function is case-sensitive, 
but we can use the "lower" function to fix it
(the reverse of this function is "upper"): """

star_system = "Alpha Centauri"
print("'a' in Alpha Centauri with first 'a': ", star_system.lower().count("a"), "\n")

"""Another solution to this problem is to replace "A" with "a". 
Let's do this with the "replace" function:"""

star_system = "Alpha Centauri"
print("'a' in Alpha Centauri with first 'a': ", star_system.replace("A", "a").count("a"), "\n")



"""An important and convenient help for beginning programmers will definitely be index reference.
It is done in square brackets, in which we specify start, end, and order
 of passing. To refer to a specific number, it is enough to write its 
 index in brackets (it always starts with zero and you should keep this in mind). """

stars = ["Sun", "Alpha Centauri", "Stephenson 2-18"]
print("Second place for: ", stars[1], "\n")

"""Lifehack. To quickly and easily change the order of the data in the list into
 the reverse order, we just need to write the following construction [::-1]
 (The "reverse" function does the same thing)."""

stars = ["Sun", "Alpha Centauri", "Stephenson 2-18"]
print("Our reverse stars: ", stars[::-1], "\n")



"""One of the most useful functions that I use most often when solving problems 
is the "len" function. It measures the length of a string and gives the number 
of objects inside the "list". Let's combine it with the function "sum" and 
calculate the number of stars and star systems: """

stars_in_system = [9, 21, 6, 13]
print("Stars in all systems: ", sum(stars_in_system), "\n"''
      "Number of systems: ", len(stars_in_system))
