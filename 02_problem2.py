# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’

class animals:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name of animal is : {self.name}")

class pets(animals):
    def __init__(self,name,petname):
        super().__init__(name)
        self.petname = petname
    def show(self):
        print(f"The name of animal is : {self.name} and the pet name is: {self.petname}")

class dog(pets):
    @staticmethod
    def bark():
        print("bow bow!")
d = dog("Dog","Buddy")
d.bark()
d.show()

e = animals("Cat")
e.show()

f = pets("Cat","Whisker")
f.show()