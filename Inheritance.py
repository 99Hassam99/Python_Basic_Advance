"""
eg
Vehicles
Usage (Transportation)
Inherited ( Bike, Truck, Car)

Benefits of inheritance
1-code reusability
2-Extensibility
3-Readability

"""
class vehicale:
    def general_usage(self):
        print("general usage: Transportation")
class car(vehicale):
    def __init__(self):
        print("Im a car")
        self.wheels=4
        self.roof=True

    def specific_usage(self):
        print("Specific use: commute to work, vacation with family")

    def specifications(self):
        #self.general_usage()
        print("Specs: 4 wheeler, auto engine, Hybrid")
class bike(vehicale):
    def __init__(self):
        print("Im a motorbike")
        self.wheels=2
        self.roof=False
    def specific_usage(self):
        print("Specific use: Road trip, racing")

    def specifications(self):
        # self.general_usage()
        print("Specs: 2 wheeler, Manual engine, Not Hybrid")
c = car()
c.general_usage()
c.specific_usage()
c.specifications()
b=bike()
b.general_usage()
b.specific_usage()
b.specifications()


"""
isinstance (built-in functions) (it will tell you if an object is an instance of a specific class or not)
and issubclass methods(built-in functions) (it will check if one class is a subclass of another or not)
"""
print(isinstance(c,bike))
print(issubclass(car,vehicale))