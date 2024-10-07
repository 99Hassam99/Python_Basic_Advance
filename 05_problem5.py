# Write a program to find the maximum of the numbers in a list using the reduce
# function.
from functools import reduce
l = [1,2,3,4,9,7]

def greater(a,b):
    if (a > b):
        return a
    return b

print(reduce(greater,l))

# debug to understand the concept