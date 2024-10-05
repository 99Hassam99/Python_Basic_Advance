# OPERATOR OVERLOADING IN PYTHON
# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)
# Other dunder/magic methods in Python:
# str__() # used to set what gets displayed upon calling str(obj)
# 45
# __len__() # used to set what gets displayed upon calling.__len__() or
# len(obj

class number:
    def __init__(self,n):
         self.n = n
# in python everything is class even an integer
# without methods overloading performing an addition function will give you an error

    def __add__(self, num):
        return self.n + num.n

    def __sub__(self, num):
        return self.n - num.n

    def __mul__(self, num):
        return self.n * num.n

    def __truediv__(self, num):
        return self.n / num.n

    def __floordiv__(self, num):
        return self.n // num.n

    def __str__(self):
        return f'number({self.n})'

    def __len__(self):
        return len(str(self.n))
n = number(1)
m = number(2)

print(n + m)
print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)
print(str(m))
print(len(m))