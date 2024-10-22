# 1. Create a custom exception AdultException.
#
# 2. Create a class Person with attributes name and age in it.
#
# 3. Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
#
# 4. Create a function display_person() which prints the age and name of a person.
#
# let us say,
#
# if age>18
#     he is major
# else
#     raise exception
#
# create cusomException named is-major and raise it if age<18.

# for making exception just make subclass of Exception
class AdultException(Exception):
    pass

class person():
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def get_minor_age(self):
        if int(self.age)>18:
            raise AdultException
        else:
            return self.age
    def display(self):
        try:
            print(f'age: {self.get_minor_age()}')
        except AdultException:
            print('person is an adult')
        finally:
            print(f'name: {self.name}')

# AdultException is raised
person('Hassam',23).display()

# No exception
person('zayan',5).display()