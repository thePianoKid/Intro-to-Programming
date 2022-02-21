# Day 1

## Why Program?

Computer science is perhaps the most applicable scientific field of our time. Computers have invaded every possible aspect of modern life: computers aid social interaction, they are instrumental in the field of medicine, they have mapped every single square meter of our planet. The list seems to be steadily approaching infinity. No matter what your career path is, a solid understand of computers and programming will aid you and differentiate you from your peers. 

Computers, essentially, are machines that clumsily imitate the beautiful complexity of the human brain. The hardware of a computer is like the fleshy part of the brain, it is the programmer’s job to fill this metal box with “thoughts”. There are very striking parallels between programming and the elves waking up the trees and teaching them to speak in Lord of the Rings.

If are not swayed by inherit beauty of computer programming, perhaps I can convince to learn to love this field using monetary incentives.

The average North American software engineer makes $150K CAD and an every-level position in Canada pays about $80K CAD. As in every field, if you are good at what you do, you will make more than the average person. For example, a senior developer at Google makes upwards of $200K per year. 

If we have some fledgling entrepreneurs in the room, programming is an invaluable skill to have. Most new businesses utilize code and there is very little overhead in the tech sector; many of the great inventions of the 21st century have been by university students working in their garage. 

In this course, I will be giving you the building blocks you will need to start your journey as a programmer. It is up to you to take these tools that I am giving you and makes something amazing. If you don’t think you have a good enough computer, always remember that the computers used to go to the moon had less computation power than a smartphone from 5 years ago.  

Thank you very, very much for your patience I hope you didn’t mind my little rant. Without further ado, let’s get programming!

<br>

## A (very) Brief History of Computing

- Before we get into programming, it is important to look down at the shoulders of the giants we are standing on. These are great men who have made it possible for you to spend hours in your room watching "Treadmill Fails - Vol 13"

- Alan Turing

    - Alan Turing was a British mathematician who taught himself higher mathematics while in high school.

    - Turing single handedly laid the foundation for modern computing in the 1920s. He invented the binary system that is still used in computers today.

    - Turing also contributed significantly to the war effort during WWII as a code breaker. Historians agree that Turing’s work in decryption shortened the War by months or even years, saving countless lives.


- Steve Wozniak and Steve Jobs

    - Steve Wozniak co-founded Apple Computers with Steve Jobs. Together, they created the first truly accessible personal computer; the Apple II.

    - The Apple II revolutionized computing and spawned a whole generation of programmers and hackers. 

    - Steve Jobs would go on to take Apple Computers to immeasurably greater heights, creating amazing new products like the iPod, iPhone and iPad. 

- Further research: George Boole, Robert Moore, Edsger Dijkstra, Bill Gates

<br>

## What is Python?

- Python is a programming language that can be installed on any computer (Windows, Mac, Linux). Python is like a bridge between the user (you) and the computer. The computer only understands ones and zeros, and humans only understand spoken languages. Python, and all other programming languages like it are kind of like a mix. Humans can pretty easily read python code, but it is certainly not like any human language. 

- There are many different ways to run Python code, we will be using two different ways.
    - First, we will look at the IDLE which can only run one python command at a time. This makes it easy to run little chunks of code, but you can’t really write a big program on it
    - Later on, we will look at creating files where we can store long programs

<br>

## Python Installation 🐍

- Visit python.org and download Python version 3.9.X

- Once Python has been downloaded onto your machine, your computer will be able to "speak" the Python programming language. 

- Enter python3 into the terminal to make sure Python was installed correctly

<br>

## The terminal (command prompt)

- The terminal is a direct connection between the user and the central processing unit of the computer 

- You enter text-based command that tell the computer exactly what to do

- Before Apple's operating system was written, the only application on a PC was the terminal

- The terminal is not used as often today because apps with windows have become more popular

- Programmers still use the terminal because it is more efficient

```bash
telnet towel.blinkenlights.nl
```

<br>

## Basic Data Types in Python 

- Data types are like different kinds of objects. In the physical world we all live in, we classify different types of objects (the word 	"car" could refer to a Jeep, a Tesla, etc). We do the same thing in coding. There are different types of "objects" that we need to 	learn about.

<br>

## Integers
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

- We call the symbols "+, -, *, ..." arithmetic operators
- The "**" symbol is the exponential operator; it raises the first number to the power of the second number
- The "%" symbol is the modulo operator, it returns the remainder after dividing the first number by the second number
- The "//" symbol performs integer division

<br>

## Floating Point Numbers
- Floating point numbers are different from integers because they contain a decimal place. For example, 3 is a integer while 		3.0 is a floating point number.
- Floating point numbers use the same arithmetic operators as integers

<br>

## Strings
- Strings are basically collections of characters that stored in a sequence
- Strings ALWAYS start with an quote symbol and end with a quote symbol
- String are useful for storing text
- We can manipulate strings using string operators
- Open up the Python IDLE and run the following commands:

```python
>>> "Hello" + "World"
>>> "Hello"*100
>>> "Hello"[0]
>>> "Hello"[0:2]
>>> "Hello"[0:2]*2
>>> "J"+"Hello"[1:]
```

- Why is it useful to manipulate strings? 
    - Getting only the last name of someone from a database
    - Printing out a customized welcome message

