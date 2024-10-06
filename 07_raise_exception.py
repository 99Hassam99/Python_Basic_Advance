# We can raise custom exceptions using the ‘raise’ keyword in python.
# some time we raise error/exception by ourselves to aware the developer about a mistake
# for example
a = int(input("Enter a nO.1 :"))
b = int(input("Enter a nO.2 :"))

if (b == 0):
    raise ZeroDivisionError ("Hey our code is not meant to divide numbers by zero.")
else:
    print(f"the division a/b is:{a/b}")



a = int(input("Enter No 1: "))
b = int(input("Enter No 2: "))

if (b==0):
    raise ZeroDivisionError ("hey our code cant divide numbers by zero.")
else:
    print(f'the division is: {a/b}')