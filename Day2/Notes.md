# Day 2

## Variables 

- Variables are words that store data

- You can think of variables as boxes that have a label
    - The label is the name of the variables, and inside the box we store the various kinds of data

- We can use the print keyword to print out the data stored in our variables to the screen

```python
>>> name = "Gabe"
>>> print(name)
```
- The print command is not only for variables. It will print out any data type you give it

- You can change variables and manipulate them

```python
>>> year = 2022
>>> print(year)
>>> new_year = year + 1
>>> print(new_year)
>>> name = "Gabe"
>>> print("Hello "+name)
```

<br>

## Saving Python Files

- Now that we have talked about the basic command you need to know to get started with Python, let’s start making some 	real programs instead of typing all these commands into the IDLE

- A computer program is simply a collection of commands that are executed one after the other

- Some computer programs only have one command in them, while others could be could contain millions of commands

- We can save programs so that we can use them for later 

- Let’s create a Python file (make sure to include the .py suffix)

- Once the program is created, let’s make our very first Python program

<br>

> hello_world.py
```python
message = "Hello world!"
print(message)
```

- Save the program, and run it using the default Python editor

- Congrats, you just wrote your first Python program 🎉
    - From now, until the end of time, that program will do that exact same thing when you run it

- Get used to this notion of making and saving files, we will be doing it A LOT

<br>

## Getting Input

- Python makes it easy to get input from the terminal
- Simply use the `input` keyword

> get_input.py
```python
user_input = input("Enter your name: ")
print("Hello, "+user_input+"!")
```

<br>

## Comments

- Comments are used to explain code
- Comments are denoted by a `#` in Python 
- When the code is run, comments are completely ignored

```python
# This is an example of a comment
# These two lines will be completely ignored
```

<br>

## If Statements

- Let’s move onto some more complex concepts in Python, starting with the if statement

- Takes in a comparison and runs different blocks of code based on the comparison. If statements are an incredibly powerful tool 	because the allow computers to "think" a little more like humans

> if_statement.py
```python
if 1 < 2:
	print("One is less than two")

if 1 > 2:
	print("One is greater than two")

if 1 > 2:
	print("One is greater than two")
else:
	print("One is not greater than two")

password = "1234"
input = "134"

if password == input:
	print("Login successful")
else:
	print("Incorrect password, try again")
```

<br>

## For Loops

- For loops repeat a block of code n times

- We will go into more depth concerning lists later, for now, just think of them as a collection of items

> for_loop.py
```python
for i in range(10):
	print("Yo dog")

counter = 0
for i in range(100):
	print(str(counter)+"bottles of beer on the wall")
	counter = counter + 1

for i in range(5):
	print(str(i)+"bottles of beer on the wall")
```

<br>

## While Loops

- While loops repeat until a condition is met

> while_loop.py
```python
user_input = input("Say uncle: ")

while (user_input != "uncle"):
    user_input = input("Say uncle: ")
```
