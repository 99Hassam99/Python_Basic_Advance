"""
decorators allow you to wrap you function in another function

Functions are first class obj in python.
What it means is that they can be treated just like any other variable,
and you can pass them as argument to another function or even
return them as a return value.
"""

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " milli seconds.")
        return result
    return wrapper

@time_it
def calc_square(numbers):
   # start = time.time() | just written it to understand the difference of decorators
    result=[]
    for number in numbers:
        result.append(number*number)
   # end =time.time()
   # print("cal_square took "+ str((end-start)*1000)+" milli seconds")
    return result

@time_it
def calc_cube(numbers):
   # start = time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
   # end = time.time()
   # print("calc_cube took " + str((end - start) * 1000) + " milli seconds")
    return result

array= range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)


