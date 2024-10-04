# __INIT__() CONSTRUCTOR
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes ‘self’ argument and can also take further arguments.
# For Example:

class Employee:
    # language ="Python" # class attribute
    # salary=120000

    def __init__(self,name,salary,language): # __xyz__ | dunder method that is call automatically
        self.name=name
        self.salary=salary
        self.language=language
        print("Im good")

    # def getInfo(self):
    #     print(f"the language is: {self.language}, and the salary is: {self.salary}")

    # @staticmethod
    # def greet(self):
    #     print("Good Morning!")

hassam = Employee("Shaq",10000,"C++")
print(hassam.language,hassam.salary,hassam.name)
# hassam.name="Hassam"
# hassam.getInfo()