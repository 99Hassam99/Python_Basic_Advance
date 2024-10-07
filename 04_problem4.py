# 4. Write a program to filter a list of numbers which are divisible by 5.
l = [25,23,34334,545445,2322,76557,121123,344343,544,44,55,45,70]
def divide(n):
    if n%5==0:
        return True
    return False

only_divisible =filter(divide,l)
print(list(only_divisible))


# method 2
def divisible(n):
    if (n%5==0):
        return True
    return False
a = [2,54,3,76,98,55,767,4554,67,67,76,233,44,555,6,7,76]
f =list(filter(divisible,a))
print(f)