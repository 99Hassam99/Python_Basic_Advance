# Single inheritance occurs when child class inherits only a single parent class.

# Base class / Parent class
class employee:
    company="ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")


# it's not a good way to write different classes because there are much chances of errors
# class programmer:
#     company="ITC"
#     def show(self):
#         print(f"The name of programmer is {self.name()} and the salary is {self.salary}")
#
#     def language(self):
#         print(f"The name  is {self.name} and he is good with {self.languag} language")
# so tp solve this issue we use a method called inheritence.
# inherited / child class
class programmer(employee):
    company="ITC tech"
    def language(self):
        print(f"The name  is {self.name} and he is good with {self.languag} language")

a =employee()
b=programmer()
print(a.company,b.company)


"""
Inheritance is a way of creating a new class from an existing class.

Syntax:
class Employee: # Base class 
# Code
class Programmer(Employee): # Derived or child class
# Code
We can use the method and attributes of ‘Employee’ in ‘Programmer’ object.
Also, we can overwrite or add new attributes and methods in ‘Programmer’ class
"""

