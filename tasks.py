import os
import sys
from tkinter import Variable 

answer = (input(" Did you drink beer? = "))
if answer.lower() == "yes":
    print("You can start coding now")
else:
     print("Drink a beer and come back")
     sys.exit(0) 

user = input("What is youe name")  #task 3
print(f"Welcome {user}")

#task 1

print("Hello python")

#task 2

name1 = "John" 
name2 = "Dave"
print(f"{name1} is eating ice cream with {name2}")

num1 = input("Give me a number = ")
num2 = input("Give me a second number = ")
add = (int(num1) + int(num2))
print(add)

#task 4 

num4 = 47 
num5 = 102 
sum = (int(num4) + int(num5))
Diff = (int(num4) + int(num5))
product =(sum * Diff)
print (num4,"+", num5, "=", sum)
print (num4,"-", num5 ,"=", Diff)
