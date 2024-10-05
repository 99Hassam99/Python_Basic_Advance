# SUPER() METHOD
# super() method is used to access the methods of a super class in the derived class.


class employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        super().__init__()
        print("constructor of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c = 3

# base class | it only has it own properties
o=employee()
print(o.a)

# child 1 | it has its own as well as parents properties
o = programmer()
print(o.a,o.b)

# child 2 | it has its own as well as parent and other child property
o = manager()
print(o.a,o.b, o.c)

