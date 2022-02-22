############## Challenge 1 ##############
# Transform the string "hello" into "jello" and print it out
print("j"+"hello"[1:])

############## Challenge 2 ##############
# Print out enough dashes to span your computer screen
# The 100 is arbitrary
print("-"*100) 

############## Challenge 3 ##############
# Get the name from a user, store it, then print it out prefixed by "Hello, "
user_name = input("Enter your name: ")
print("Hello, "+user_name)

############## Challenge 4 ##############
# Get the name from a user, store it, then print it out prefixed by "Hello, "
# Then add a specified number of exclamation marks at the end

user_name = input("Enter your name: ")
num_marks = input("Enter the number of exclamation marks: ")
num_marks = int(num_marks)

print("Hello, "+user_name+"!"*num_marks)

############## Challenge 5 ##############
# Perform divison on two numbers and print out the whole quotient and the remainder
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2)

quotient = num1//num2
remainder = num1%num2

quotient = str(quotient)
remainder = str(remainder)
num1 = str(num1)
num2 = str(num2)

print(num1+" divided by "+num2+" is "+quotient+" with a remainder of "+remainder)
