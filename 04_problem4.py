# 4. Write a recursive function to calculate the sum of first n natural numbers.
"""
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(5)=1+2+3+4+5
sum(n)=1+2+3+4+5...n -1+n
sum(n)=sum(n-1)+n
"""
def sum(n):
    if (n == 1): # base condition which doesn’t call the function any further.
        return 1
    return sum(n-1)+ n #  function calling itself

n = int(input("Enter a number: "))
print(f'The factorial of this number is: {sum(n)}')
