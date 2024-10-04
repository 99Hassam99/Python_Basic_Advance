# self refers to the instance of the class. It is automatically passed with a function call
# from an object.
# harry.getSalary() # here self is harry
# equivalent to Employee.getSalary(harry)
# self is important for every method created, if we use it or not
# we can use other name for self but self is by default and well cleared.

class Employee:
    language ="Python" # class attribute
    salary=120000

    def getInfo(self):
        print(f"the language is: {self.language}, and the salary is: {self.salary}")

    def greet(self):
        print("Good Morning!")

hassam = Employee()
hassam.language="Dart" # instance attribute. It's for a particular person, it will not affect other attributes

# hassam.getInfo() # this and
hassam.greet()
Employee.getInfo(hassam) # this are same