x=input("Enter No.1:")
y=input("Enter No.1:")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception:")
    z=None
except TypeError as e:
    print("Type error exception")  #Google "python builtin exceptions" to see the list  of standard exceptions in python
    z=None
print("Division is:",z)