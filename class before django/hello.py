# if 5>2:
#     print("Five is greater than two!") #comment

# x = 5
# y = "Hello, World!"
# print(x)
# print(y)

# age = 36
# my_name = "John"

# Age = 40
# AGE = 42

# not allowed
# ==============
# 2age = 40
# my-name = "John"
# my name = "John"


# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"
# print("x = ", x)


# global variable
# ===============  
# x = "Hello"
# print(type(x))
# def myfunc():
#     global x
#     x = "fantastic"
#     print("IN FUNCTION " + x)
# myfunc()
# print("Python is " + x)

# x = "3.1"
# # y = int(x)
# z = float(x)
# # print(y)
# print(z)

# import random
# print(random.randrange(1, 6))

# strings are array
# a = "Hello World"
# print("Hello" not in a)
# print(len(a))
# print(a.replace("H", "J"))
# print(a.lower())
# print(a[2:5])

# myorder = "I want {1} pieces of item {0} for {2} dollars."
# print(myorder.format("apple", 10, 3))

# txt = "We are the so called \"Vikings\" from the north."
# print(txt)

# x = "Hello World"
# print(bool(x))
# print(bool(["apple", "banana", "cherry"]))

from Module import greeting
import camelcase

c = camelcase.CamelCase()
txt = greeting("John")
print(c.hump(txt))
# name = person["age"]
# print(name)
