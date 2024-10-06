# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError


try:
    a=int(input("Enter a number 1: "))
    b=int(input("Enter a number 2: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite by handling")