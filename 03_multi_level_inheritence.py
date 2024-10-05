# MULTILEVEL INHERITANCE
# When a child class becomes a parent for another child class.

# syntax of multilevel inheritance

# parent class
class employee:
    a = 1
# child 1
class programmer(employee):
    b = 2
# child 2
class manager(programmer):
    c = 3

# base class | it only has it own properties
o=employee()
print(o.a) # prints the attribute "a"
# print(o.b) # gives an error because there is no attribute "b" in Employee class.

# child 1 | it has its own as well as parents properties
o = programmer()
print(o.a,o.b)

# child 2 | it has its own as well as parent and other child property
o = manager()
print(o.a,o.b, o.c)