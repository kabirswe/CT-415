# # Multiple Inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# class Student():
#     def __init__(self, name, age, rollno):
#         super().__init__(name, age)
#         self.rollno = rollno
# class Employee(Person, Student):
#     def __init__(self, name, age, position):
#         super().__init__(name, age)
#         self.position = position

#     def myEmployee(self):
#         print("my age is ", self.age, "And my position is ", self.position)

# x = Employee("John", 36, "Manager")
# x.myfunc()
# x.myEmployee()

# Multilevel Inheritance
# class Person:
#     pass

# class Student(Person):
#     pass

# class Employee(Student):
#     pass

# Encapsulation
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def display(self):
#         print("Hello my name is " + self.name)
#         print("My age is " + str(self.__age))
    
#     def getAge(self):
#         return self.__age
    
#     def setAge(self, age):
#         self.__age = age

# person = Person("John", 36)
# person.display()
# print(person.name)
# print(person.setAge(45))
# print(person.getAge())

# polymorphism
class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

def flying_test(bird):
    bird.fly()
    bird.swim()

parrot_var = Parrot()
penguin_var = Penguin()

flying_test(parrot_var)
flying_test(penguin_var)