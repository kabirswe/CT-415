# age = 15
# if age < 18:
#     print("Young")
# elif age > 18 and age < 50:
#     print("adult")
# else:
#     print("old")

# a = 2
# b = 3
# print("a") if a > b else print("b")

# if a > b:
#     print("a")
#     if a > b:
#         pass
#     print("a")
# else:
#     print("b")

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         print("i is 3")
#         continue
#     i += 1

# test 1
# python program to check if a number is odd or even

# test 2
# python program to check if year is leap year or not

# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

# class Person:
#     def __init__(myself, name, age):
#         myself.name = name
#         myself.age = age
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def myEmployee(self):
        print("my age is ", self.age, "And my position is ", self.position)

x = Employee("John", 36, "Manager")
x.myfunc()
x.myEmployee()