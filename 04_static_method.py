# STATIC METHOD
# Sometimes we need a function that does not use the self-parameter. We can define a
# static method like this:


class Employee:
    language ="Python" # class attribute
    salary=120000

    def getInfo(self):
        print(f"the language is: {self.language}, and the salary is: {self.salary}")


    @staticmethod
    def greet():  # greet was a function and we pass it a whole object
        print("Good Morning!")
    # def greet(self):  # greet was a function and we pass it a whole object
    #     print("Good Morning!")


hassam = Employee()
hassam.language="Dart" # instance attribute. It's for a particular person, it will not affect other attributes

# hassam.getInfo() # 1 this and
Employee.getInfo(hassam) # and 1 are same

# but if we want to not pass a whole object to the function that we dont have to pass it the whole
# object of a class (self)
hassam.greet() # greet object

# it means that greet function is a static method, and it does not need an object(self)
# without static method it will give an error without a self object

# @staticmethod is a decorator, with the help of this we marked it as a static function which means
# it will not take objects from the class, and it's an independent static function