"""All the standard library classes (so that we don't have to reinvent the wheel),
frameworks, and programs consist of manually written functions.
They are called "definitions" or "def" for short. To use it, you most often need
to fulfill several conditions: first, the function must return something; second,
something must be passed into the program. In some cases this is not required,
then "pass" is used instead of return value, and nothing is passed instead of arguments.
Let's look at the standard way of using functions. To do this, we need to declare its name,
specify the arguments to pass, spell out the actions it will perform and return
the result of these actions. It is done like this: """


def forest(tree_numbers):
    return tree_numbers * 200000  # average number of leaves on the tree


print(f"There are {forest(30)} leaves in the forest\n")

"""Above we created a function, gave it a name (forest), created a variable (tree_numbers), 
wrote the condition "return" which returns the multiplication of the variable by 200000, 
below we simultaneously passed values (30) to the function and displayed the result of the function. 

The beauty of functions is that they can perform specific tasks: divide numbers, 
process strings in a certain way, work with data. And, when you need to do certain 
things with data in a program, all you have to do is call a certain function. 
Actually, we can complicate functions as much as we want, but in the world of programming, 
there is a principle that functions should not be too large. 

However, what do we do if we don't know the exact number of arguments we will 
pass to the function. We have "*args" and "**kwargs" to help us. They work quite simply: 
"args" takes all the arguments and shoves them into "tuple".  "Tuple" is about the 
same variable as "list", except that it is immutable and ordered.
This means that we cannot change (as easily as with "list") the order inside 
"tuple" and we cannot add new data inside. "**kwargs", on the other hand, puts 
all arguments inside the dictionary. Let's look at a small example on the subject:
"""


def cars(*args, **kwargs):
    best_prices = {}
    counter = 0
    for item in args:
        best_prices[f"{item}"] = min(list(kwargs.values())[counter])
        counter += 1
    return best_prices


result = cars("toyota", "bmw", "mercedec", prices_toyota=(4000, 5000, 6000),
              prices_bmw=(3000, 6000, 7000), prices_mercedec=(3500, 7000, 6500))

print(result)

"""Let's go through the program and figure out what it does. For the sake of argument, 
the program gets brands of cars and their prices in different parts of the world, 
and returns the best prices for which they can be bought. 

Now, what about the program itself. In it, we input two variables "args" and "kwargs",
by the way, they can have any name. Then we create a dictionary, which we will return 
as the final value. We create a counter, which will help us move through the 
input dictionary. Next we go through all the car brands and find the lowest prices 
from the list for them. To do this, we use the function "min", as well as the function 
"list" together with the function "values", so that we have the possibility to 
refer to the value by index. After the cycle is finished, we return 
the resulting dictionary with the lowest prices. """

