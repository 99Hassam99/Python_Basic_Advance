# Decorators
# Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:
#
# Create a factorial function which finds the factorial of a number.
#
# Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
#
# example:
#
#     factorial(1.354) : raise Exception or print error message
#     factorial(-1) : raise Exception or print error message
#     factorial(5) : 60

def check(f):
    def helper(x):
        if isinstance(x,int)  and x>0:
            return f(x)
        else:
            raise Exception("argument is not non negative integers.")
    return helper
@check
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n* factorial(n-1)

for i in range(1,10):
    print(i,factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    print(e)

try:
    print(factorial(1.354))
except Exception as e:
    print(e)