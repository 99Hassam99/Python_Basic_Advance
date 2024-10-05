# MULTIPLE INHERITANCE
# Multiple Inheritance occurs when the child class inherits from more than one parent
# classes.

class Employee:
    company ="ITel"
    name = "Hassam"
    salary = 120000
    def show(self):
        print(f'the name of Employee is: {self.name} , and the salary is: {self.salary}')

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all languages, here is your langugae: {self.language}")

class programmer(Employee,coder):
    company="ITel"
    def showLanguage(self):
        print(f'The company name is:{self.company} and he is good with {self.language} language')

a =Employee()
b=programmer()

b.show()
b.showLanguage()
b.printLanguage()