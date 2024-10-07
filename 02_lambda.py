# Function created using an expression using ‘lambda’ keyword.

# basic example of creating square
def square(n):
    return n*n
print(square(5))

# but we can do it easily by using lambda function

square = lambda x: x*x
print(square(2))

sum = lambda a,b,c: a+b+c
print(sum(1,2,3))