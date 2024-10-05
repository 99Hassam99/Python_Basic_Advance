# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.
# Syntax:
# @classmethod
# def(cls,p1,p2):


class employee:
    a=1

    @classmethod
    def show(cls): # we can use cls for self.
        print(f"The class attribute of a is {cls.a}")

b =employee()
b.a=45
b.show()