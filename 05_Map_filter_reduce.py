# "Map" applies a function to all the items in an input_list.

# Syntax.
# map(function, input_list)
# # the function can be lambda function
l = [1,2,3,4,5]
square = lambda x : x*x
sqList = map(square, l)
print(list(sqList))


# "Filter" creates a list of items for which the function returns true.
# list(filter(function))
# # the function can be lambda function
l = [1,2,3,4,5]
def even(n):
    if (n%2==0):
        return True
    return False
only_even = filter(even,l)
print(list(only_even))


# "Reduce" applies a rolling computation to sequential pair of elements.
# from functools import reduce
# val=reduce (function, list1)
# # the function can be lambda function

# for reduce we have to import it from functools
from functools import reduce
l = [1,2,3,4,5]
def sum(a,b):
    return a + b
mul = lambda x,y : x*y
print(reduce(sum, l))
print(reduce(mul,l))
# from the list it will first add:
# l = [1,2,3,4,5] # for addition
# 1+2= 3, 3+3=6, 6+4=10, 10+5= 15
# output = 15
# l = [1,2,3,4,5] # for multiplication
# 1*2 = 2, 2*3 = 6, 6*4 = 24, 24*5 = 120
# output = 120