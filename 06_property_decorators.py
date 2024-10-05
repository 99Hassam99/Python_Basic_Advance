# @PROPERTY DECORATORS
# Consider the following class:
# class Employee:
# @property
# def name(self):
# return self.ename
# If e = Employee() is an object of class employee, we can print (e.name) to print the
# ename by internally calling name() function.


# @.GETTERS AND @.SETTERS
# The method name with ‘@property’ decorator is called getter method.
# We can define a function + @ name.setter decorator like below:

class emp: # encapsulation
    a =1
    @classmethod
    def show(cls):
        print(f'The class attribute is {cls.a}')

    # abstraction with property
    @property
    def name(self): # getter for name
        return f'{self.fname} {self.lname}'

    @name.setter
    def name(self,value): # setter for name
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# it's the concept of encapsulation and abstraction.
# abstraction means hiding implementation details from the user and encapsulation means
# packing alot of working components in a particular unit called class/

e = emp()
e.a =45

e.name = "Hassam Ahmad "
print(e.fname,e.lname)

e.show()