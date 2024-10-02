"""
Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function

factorial(0)=1
factorial(1)=1
factorial(2)=1*2
factorial(3)=1*2*3
factorial(4)=1*2*3*4
factorial(5)=1*2*3*4*5
factorial(n)=n * n-1 * ......3 * 2 * 1

factorial(n)= n * factorial(n-1)

The programmer needs to be extremely careful while working with recursion to ensure
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
direct way to code an algorithm
"""

def factorial(n):
    if (n == 1 or n == 0): # base condition which doesn’t call the function any further.
        return 1
    return n * factorial(n-1) #  function calling itself

n = int(input("Enter a number: "))
print(f'The factorial of this number is: {factorial(n)}')
