# numpy : iterate numpy array using nditer | numpy nditer

import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

"""
This method is long with 2 for loops
for row in a:
    print(row)
    for cell in row:
        print(cell)
we can use a flatten function to make it to 1 for loop
"""

# for cell in a.flatten():
#     print(cell) # same result
# we can achieve this same step by using nditer

for x in np.nditer(a,order="C"): # c is used for column order
    print(x) # same result

for x in np.nditer(a,order="F"): # F is used for Fortran order
    print(x)

"""
The C-order goes through the columns from index 0to4 then next row column
while Fortran-order goes through each row and then next column row
"""

# for Fortran order if we want to print the entire column we use flags i-e
for x in np.nditer(a,order="F",flags=['external_loop']): # F is used for Fortran order
    print(x)

# for iterating through array and to modify it we use readwrite

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
print(a) # it will square the original array


# to iterate through 2 different arrays simultaneously

a = np.arange(12).reshape(3,4)
print(a)
b = np.array((3,15,4)).reshape(3,1)
print(b)
for x,y in np.nditer([a,b]):
    print(x,y)


"""
2-D arrays are compatible when they are
either equal or
one of them is 1
"""