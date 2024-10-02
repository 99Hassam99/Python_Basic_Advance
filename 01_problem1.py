# 1. Write a program using functions to find greatest of three numbers.

def great():
    a= int(input("Enter a number: "))
    b= int(input("Enter a number: "))
    c= int(input("Enter a number: "))
    if (a>b and a>c):
        print("Greatest number is A")
    elif(b>a and b>c):
        print("Greatest number is B")
    elif(c>a and c>b):
        print("Greatest number is C")

great()

# example 2
def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=1
b=2
c=3
print(greatest(a,b,c))