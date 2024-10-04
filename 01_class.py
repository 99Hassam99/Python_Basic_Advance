"""
Solving a problem by creating object() is one of the most popular approaches in
programming. This is called object-oriented programming.
This concept focuses on using reusable code (DRY Principle).

A class() is a blueprint for creating object.


An object() is an instantiation of a class. When class is defined, a template (info) is
defined. Memory is allocated only after object instantiation.
Objects of a given class can invoke the methods available to it without revealing the
implementation details to the user. – Abstractions & Encapsulation!

"""




class Employee: # syntax of class
    salary=10000 # class attribute
    language="Python" # class attribute

# Hassam is an object 
Hassam =Employee()
Hassam.name="Hassam" # Object/instance attribute
print(Hassam.language,Hassam.name,Hassam.salary)

Hashir =Employee()
Hashir.name="Hashir"
print(Hashir.salary,Hashir.name,Hashir.language)


# here name is an object/instance attribute and salary and language are class attribute
# because they directly belong to the class
