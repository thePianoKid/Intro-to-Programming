# Day 1

## Why Program?

- Every single field has been affected by the digital revolution of the 21st century. Any career will be enhanced by a solid 	understanding of programming.

- Programming is also a relatively new field, so it’s purity has not yet been ruined by musty old men imposing nonsensical 	regulations and “best practises”.

- Also… 💰
    - The average software engineer makes $150K CAD
    - Average software developer at Google makes $190K CAD
    - Most of the gigantic multi-billion dollar companies are software-based
        - Facebook
        - Amazon
        - Netflix
        - Google

<br>

## A (very) Brief History of Computing

- Before we get into programming, it is important to look down at the shoulders of the giants we are standing on. These are great 	men who have made it possible for you to spend hours in your room watching “Treadmill Fails - Vol 13”

- Alan Turing

    - Alan Turing was a British mathematician who taught himself higher mathematics while in high school.

    - Turing single handedly laid the foundation for modern computing in the 1920s. He invented the binary system that is still 		used in computers today.

    - Turing also contributed significantly to the war effort during WWII as a code breaker. Historians agree that Turing’s work in 		decryption shortened the War by months or even years, saving countless lives.


- Steve Wozniak and Steve Jobs

    - Steve Wozniak co-founded Apple Computers with Steve Jobs. Together, they created the first truly accessible personal 		computer; the Apple II.

    - The Apple II revolutionised computing and spawned a whole generation of programmers and hackers. 

    - Steve Jobs would go on to take Apple Computers to immeasurably greater heights, creating amazing new products like the 		iPod, iPhone and iPad. 

- Further research: George Boole, Robert Moore, Edsger Dijkstra, Bill Gates

<br>

## What is Python?

- Python is a programming language that can be installed on any computer (Windows, Mac, Linux). Python is like a bridge between 	the user (you) and the computer. The computer only understands ones and zeros, and humans only understand spoken languages. 	Python, and all other programming languages like it are kind of like a mix. Humans can pretty easily read python code, but it is 	certainly not like any human language. 

- There are many different ways to run Python code, we will be using two different ways.
    - First, we will look at the IDLE which can only run one python command at a time. This makes it easy to run little chunks of 		code, but you can’t really write a big program on it
    - Later on, we will look at creating files where we can store long programs

<br>

## Python Installation 🐍

- Visit python.org and download Python version 3.9.X

- Once Python has been downloaded onto your machine, your computer will be able to “speak” the Python programming language. 

- Enter python3 into the command prompt to make sure Python was installed correctly

## Basic Data Types in Python 

- Data types are like different kinds of objects. In the physical world we all live in, we classify different types of objects (the word 	“car” could refer to a Jeep, a Tesla, etc). We do the same thing in coding. There are different types of “objects” that we need to 	learn about.


### Integers
- You may know of integers from math: they are whole numbers without any decimals places. Python is very good at working 		with integers; we can do all sorts of calculations. 
- Open up the Python IDLE and run the following commands:

```python
>>> 9+3
>>> 9-3
>>> 9*3
>>> 9/3
>>> 9**3
>>> 9%2
>>> 9//2
```

- We call the symbols "+, -, *, ..." arthmetic operators
- The "**" symbol is the exponential operator; it raises the first number to the power of the second number
- The “%” symbol is the modulo operator, it returns the remainder after dividing the first number by the second number
- The “//” symbol performs integer division

### Floating Point Numbers
- Floating point numbers are different from integers because they contain a decimal place. For example, 3 is a integer while 		3.0 is a floating point number.
- Floating point numbers use the same arithmetic operators as integers

### Strings
- Strings are basically collections of characters that stored in a sequence
- Strings ALWAYS start with an quote symbol and end with a quote symbol
- String are useful for storing text
- We can manipulate strings using string operators
- Open up the Python IDLE and run the following commands:

```python
>>> “Hello” + “World”
>>> “Hello”*100
>>> “Hello”[0]
>>> “Hello”[0:2]
>>> “Hello”[0:2]*2
>>> “J”+”Hello”[1:]
```

- Why is it useful to manipulate strings? 
    - Getting only the last name of someone from a database
    - Printing out a customized welcome message

