"""The first thing you need to understand about python is the variables.
Variables are needed for mathematical and logical operations on which all program code is based.

In computer memory, variables are references to data.
So, for example, two variables with the same value will point to the same memory location.
This can be proven with the command "id".

Let's start with this command.
First, we need to create two variables with the same value and use the "id" command on them.
This is how it's done: """

first_variable = 8
second_variable = 8

"""If we just run the code, what python will do is write the data inside the defined 
cells and store the references to them. However, we need to make sure that it does! 
To do this we will use two functions at the same time. 
First we have the function "print", and in its parentheses we will write what we want to print: 
this will be the result of the next function id, which shows us the address of the memory cell of the variable. 
"""

print(id(first_variable))
print(id(second_variable))

"""Now that we know how to use functions (of course this is not the only way to use them, but first things first), 
let's move on to types of variables. In Python there are several types: "int" stores integers, 
"float" stores numbers with decimal places, "str" stores characters, "bool" stores True or False, 
"list" stores any set of data listed above or below, and "dic" stores pairs (like in a dictionary). 
These are not all the variables that Python has, but we will stop there for now.

Each of the variables in Python has its own set of features. We won't look at them in detail for the moment, 
but focus on the main ones. In order to familiarize ourselves with the list of variables, 
let's make a program for changing a person's temperature. It will look like this: """

first_name = 'Artem'
age = 27
temperature = 36.6
ill_status = False
body_characteristics = {"Wheight": 80, "Height": 190}
doctors_name = ["Jhon", "Anne", "Nickolas"]

print(f"\nFirst name: {first_name}\n"
      f"Age: {age}\n"
      f"Temperature: {temperature}\n"
      f"Ill_status: {ill_status}\n"
      f"Body_characteristics: {body_characteristics}\n"
      f"Doctors_name: {doctors_name}")

"""Let's go through the program and see what it does. We create 6 variables and output them. 
For now, we'll take the peculiarities of variable reflection as a given. In the "print" function, 
we put an "f" in front of the quotes; we need it to use the values of the variables themselves inside the text. 
Also, we add \n inside the quotes, which allows us to skip to a new line instead of typing the text as a monolith."""

"""Once we are familiar with variables, I suggest we move on to operators. 
Operators are essentially actions on variables. So let's walk through them and see how they differ. """

Num = 8           # assignment operator =
Num = 8 + 7       # addition +
Num = 8 - 7       # subtraction -
Num = 8 * 7       # multiplication *
Num = 8 ** 7      # exponentiation **
Num = 8 / 7       # division /
Num = 8 // 7      # integer division //
Num = 8 % 7       # finding the remainder of a division %
Num = 8 > 7       # operator more >
Num = 8 < 7       # operator less <

