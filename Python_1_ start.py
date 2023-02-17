"""The first thing you need to understand about python is the variables.
Variables are needed for mathematical and logical operations on which all program code is based.

In computer memory, variables are references to data.
So, for example, two variables with the same value will point to the same memory location.
This can be proven with the command "id".

Let's start with this command.
First, we need to create two variables with the same value and then use the "id" command on them.
This is how it's done:"""

first_variable = 8
second_variable = 8


"""If we just run the code, what python will do is write the data inside the defined 
cells and store the references to them. However, we need to make sure that it does! 
To do this we will use two functions at the same time. 
First we have the function "print", and in its parentheses we will write what we want to print: 
this will be the result of the next function id, which shows us the address of the memory cell of the variable. """

print(id(first_variable))
print(id(second_variable))

"""Now that we know how to use functions (of course this is not the only way to use them, but first things first), 
let's move on to types of variables. In Python there are several types: "int" stores integers, 
"float" stores numbers with decimal places, "str" stores characters, "bool" stores True or False, 
"list" stores any set of data separated by commas, and "dic" stores pairs (like in a dictionary). 
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
In the "print" function, we put an "f" in front of the quotes; we need it to use the 
values of the variables themselves inside the text. Also, we add \n inside the quotes, 
which allows us to skip to a new line instead of typing the text as a monolith."""

"""Once we are familiar with variables, I suggest we move on to operators. 
Operators are essentially actions on variables. So let's walk through them and see how they differ. """

Num = 8           # Assignment operator =
Num = 8 + 7       # Addition +
Num = 8 - 7       # Subtraction -
Num = 8 * 7       # Multiplication *
Num = 8 ** 7      # Exponentiation **
Num = 8 / 7       # Division /
Num = 8 // 7      # Integer division //
Num = 8 % 7       # Finding the remainder of a division %

"""Lifehack. If we do not want to assign a new value to a variable, 
as we just did, but rather add an existing value inside it, we can use this abbreviated construction:  """

Num = 1
Num_two = 2

Num += Num_two      # Addition +
Num -= Num_two      # Subtraction -
Num *= Num_two      # Multiplication *
Num **= Num_two     # Exponentiation **
Num /= Num_two      # Division /
Num //= Num_two     # Integer division //
Num %= Num_two      # Finding the remainder of a division %

"""So far we have been dealing with cases where a variable is assigned a certain value, but it is 
possible to use operators to set conditions to functions. For example, let's take the 
"if" function (in true it cals conditional statement). """

if Num > Num_two:
      print("Num bigger then Num_two")

"""In this function, we used a comparison operator, after which we wrote the condition that will be 
executed if the condition is True. Comparison operators can be different, for example: """

Num > Num_two      # Operator more >
Num < Num_two      # Operator less <
Num >= Num_two     # Operator more or equal >
Num <= Num_two     # Operator less or equal <
Num != 8           # Operator not equal
Num == 8           # Operator equal

"""In addition, we can add an additional condition to our function. This is done like this: 
"elif" is responsible for a separate case from "if", and "else" is responsible for all other cases. """

if Num > Num_two:
      print("\nNum is bigger then Num_two")
elif Num < Num_two:
      print("\nNum is smaller then Num_two")
else:
      print("\nNumbers are equal") # which follows logically

"""We can complicate our "if" conditions with the logical operators "and", "or", "not". 
"And" is responsible for the equality of two conditions at once, "or" returns True if 
at least one condition is met, while "not" returns False when the condition is met and 
True when the condition is not met. We can use them in the following way:"""

if Num > Num_two and Num > 0:
      print("\nNum is bigger then Num_two and 0")
elif Num < Num_two or Num < 0:
      print("\nNum is smaller then Num_two or 0")
elif not Num < Num_two:
      print("\nNum is bigger then Num_two")

"""Returning to comparison operators, we can use them inside the value 
assignment operation, where the value will be assigned True or False: """

Num = 8 < 7
Num = 8 > 7
Num = 8 <= 7
Num = 8 >= 7
Num = 8 != 7
Num = 8 == 7