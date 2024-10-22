# 1. create inheritance using animal Dog relation.
# for example,
#     Animal and Dog both has same habitat so create a method for habitat

# 2. use super() constructor for calling parent constructor.
# class Animal:
#     #code
#
# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.

class animal:
    def __init__(self,habitat):
        self.habitat= habitat
    def print_habitat(self):
        print(self.habitat)
    def sound(self):
        print('some animal voice')

class Dog(animal):
    def __init__(self):
        super().__init__('kennel')

    def sound(self):
        print('woof woof!')

x = Dog()
x.print_habitat()
x.sound()