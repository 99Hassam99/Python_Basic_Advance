# 6. Write a python function which converts inches to cms.

def inches_cms():
    inches=int(input("Enter a number:"))
    centimeter = 2.54
    conversion = inches*centimeter
    print(conversion)
inches_cms()



# example 2

def inches_cms(inches):
    return inches*2.54

n=int(input("Enter value in inches: "))
print(f'The value in cms is:{inches_cms(n)}')