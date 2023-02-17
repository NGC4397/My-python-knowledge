"""Now we come to such an important topic in the programming world as loops.
Loops are the basis of most things in programs. They are a handy, and most importantly,
 very powerful tool for data processing.

The main representative of loops is "for". This is used, for example,
when we need to go through all letters of a word and compare values, 
or when we need to process an array of data and want to do it from the beginning to the end.
Often the "for" loop goes together with the logical "in" operator.
This operator returns True if the value is in the data array. For example,
if the letter "a" is in the word "star". Let's see how a loops works in practice."""

letter = "star"
for item in letter:
    print(item)

print("\n")

"""We did some important things in our program. First, we created a variable called "letter" 
and placed a value inside it. Second, we wrote a loop, which consists of several things:
the loop designation itself "for", the iterated variable "item", the logical operator "in", 
the variable whose value we will pass over, and a condition that will be repeated until the 
letters assigned to the variable run out.  

It should be noted that the variable "item" can be designated by any word, but I got used 
to this designation, because I think it is universal. 

Another way to use the "for" loop is to use it together with the "range" function. 
Let's look at this variant in practice:"""

number_of_stars = 4
for item in range(number_of_stars):
    print(f"{item} star")

print("\n")

"""It should be noted that the "for" loop is one of the most voracious in terms of 
memory consumption and computation speed. Calculation speed and working with memory are 
a separate topic, which we will return to in the following chapters. 
I would advise you to avoid the for loop if possible if you're working with large data sets. 
You can often replace the "for" loop with the "while" loop. This is what we will move on to. 

"While" can be understood literally by its own abbreviation. 
 Its syntax is as follows: as long as the designated condition is met, these actions will be performed. 
 For example:"""

number = 4
while number > 0:
    print(f"{number} - 1")
    number -= 1

print("\n")

"""We can use several loops, conditional statements in the same code area. 
However, we must be careful with nested loops. For example, two nested "for" 
loops can be the most difficult place in a program. 
In sports programming, two nested loops would immediately add a complexity of O(N*2) to a program. 
When designing an algorithm, you should aim (ideally) at O(N), i.e., at the absence of nested loops. 
For an example of nested loops, let's consider the following program:"""

number_of_stars = 4
for item in range(number_of_stars):
    if item %2:
        print(f"I found the twin stars")

"""Our program is almost identical to the example before last, 
but inside the for loop we have added a condition that checks if the value is a multiple of two. 
In order for us to be able to use our functions several times, there are "Definition" functions. 
They represent the next chapter of our tutorial, to which I suggest we skip. """

