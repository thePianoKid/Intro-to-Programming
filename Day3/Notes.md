# Day 3

## Functions

- Functions are like little machines that take in something and spit something else out

- The function takes in things called parameters that are specified by the programmer

- The function returns some value 

> my_first_function.py
```python
def sum(a, b):
    return a + b

sum(1, 1)
```

- Some functions don't return anything at all

```python
def can_vote(age):
    if (age < 18):
        print("You are not allowed to vote because you are under 18 years old")
    else:
        print("You are allowed to vote because you are over 18 years old")

can_vote(17)
can_vote(110)
```

- Some functions don't take any parameters and don't return anything

```python
import requests

def iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url).json()

    print("Longitude: "+response["iss_position"]["longitude"])
    print("Latitude: "+response["iss_position"]["latitude"])

iss_position()
```

- It is a good idea to include a docstring whenever you make a function

- A docstring explains what the function does and outlines its parameters
    - There are different ways to format the docstring, I like [Google Style Python Docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html)

```python
def sum(a, b):
    """This function returns the sum of two numbers
    
    Args:
        a (float): first number
        b (float): second number
    
    Returns:
        float: sum of two arguments
    """
    return a + b
```

<br>

## Libraries

- Programmers REALLY like sharing code
- Python makes it easy to use other people's code, and (as an added bonus) it's not stealing 
- Using the `import` keyword, we can load tons of code into our program

- For example, we can use the Turtles library to draw shapes using Python

```python
from turtle import *

for i in range(4):
        forward(100)
        right(90)

done()
```

```python
from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    
    if abs(pos()) < 1:
        break

end_fill()
done()
```
