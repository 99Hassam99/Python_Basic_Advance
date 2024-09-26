"""
What is class?
Properties and methods form a central entity called a class
eg,
Human (class)
2 components
properties(Name Gender Occupation)
Methods( Speaks  do work sleep)

So class is nothing but an abstraction of some entity which contains common set of properties and methods
"""

"""
What is Object?
An object is nothing but a specific instance of a class 
eg:
for human beings these 2 Tome cruise and Babar Azam are two instances of the human class 
"""


class Human:
    def __init__(self, Name, Gender, Occupation):
        self.Name=Name
        self.Gender=Gender
        self.Occupation=Occupation

    def do_work(self):
        if self.Occupation == "Wushu Player":
            print(self.Name,"Plays Wushu")
        elif self.Occupation == "Student":
            print(self.Name,"Do Studies")

    def speaks(self):
        print(self.Name,"Says! How are you?")

    def Sex(self):
        if self.Gender == "Male":
            print(self.Name,"is Male")
        elif self.Gender == "Female":
            print(self.Name,"is Female")

shaq=Human("Hassam","Male","Wushu Player")
shaq.do_work()
shaq.speaks()
shaq.Sex()

eman=Human("Eiman","Female","Student")
eman.do_work()
eman.speaks()
eman.Sex()