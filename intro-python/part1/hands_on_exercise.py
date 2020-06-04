"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("type = ", type(pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
   print(i, "is less than 50")
else:
   print(i, "is greater than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == "orange":
   print("You have an orange")
elif picked_fruit == "red":
   print("You have a strawberry")
else:
   print("Your stuck with a yellow banana")
   
   

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiplyit(x,z):
    y = x * z
    return y
    
# TODO: Now call the function a few times to calculate the following answers
y = multiplyit(12,96)
print("12 x 96 =",y)
y =  multiplyit(48,17)
print("48 x 17 =",y)

y = multiplyit(196523,87323)
print("196523 x 87323 =",y)
