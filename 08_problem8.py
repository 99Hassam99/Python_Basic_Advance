# 8. Write a python function to print multiplication table of a given number.

def multiplication(n):
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')

n=int(input("enter a number:"))
multiplication(n)