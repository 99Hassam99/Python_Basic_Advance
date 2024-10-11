import numpy as np

a =np.array([5,6,9]) # one dimensional array
print(a[0])
print(a[1])
print(a[2])
print("Dimensions:",a.ndim)
print("bitesize:",a.itemsize)
print(a.dtype)

b =np.array([[5,6],[1,2],[3,4]]) # two-dimensional array
print("Dimensions:",b.ndim) # tell about dimension of array
print("bitesize:",b.itemsize)
print(b.dtype) # tell about datatype

# for different datatype ther than int we can write as

b =np.array([[5,6],[1,2],[3,4]], dtype=np.float32)
print("bitesize:",b.itemsize)


b =np.array([[5,6],[1,2],[3,4]], dtype=np.float64)

print("bitesize:",b.itemsize) # print item-size in bytes

print(b)
print(b.size) # print size of b

b =np.array([[5,6],[1,2],[3,4]], dtype=complex) # complex datatype
print(b)

b=np.zeros((3,4)) # print zero's with 3 rows and 4 columns
print(b)

b=np.ones((3,4)) # print one's with 3 rows and 4 columns
print(b)

l = range(5)
print(l)
print(l[0],l[1],l[2],l[3],l[4])

l = np.arange(0,5) # it will print an array ranges from index 0-4
print(l)

l = np.arange(0,5,2) # 2 defines number of step or jumping or skiping 2 steps
print(l)

l=np.linspace(1,5,10) # linear sequence of numbers, space between 1 and 5
print(l)




c =np.array([[1,2],[3,4],[5,6]])
print(c)

print("shape:",c.shape) # output: (3,2) means 3 rows and 2 columns
reshape_c =c.reshape(3,2)
print("reshape:",reshape_c)

rav_c=c.ravel() # for flatting the array
print("flatten: ",rav_c) # it's not going to change the original array

print("low:",c.min()) # print the lowest number of array
print("high:",c.max()) # print the highest number of array

print("sum:",c.sum()) # sum all the numbers in an array list

print(c)
print("row axis=0:",c.sum(axis=0)) # it will add numbers row wise
print("column axis=1:",c.sum(axis=1)) # it will add numbers column wise
"""
example:
c= [1 2]
   [3 4]
   [5 6]
axis=0 will add 1,3,5 = 9 &&  2,4,6 = 12 i-e [9 12]
axis=1 will add 1,2=3 && 3,4=7 && 5,6=11 i-e [3,7,11]
"""

print("square root: ",np.sqrt(c)) # find square root

print(f"the standard daviation of {c} is: {np.std(c)}") # find standard daviation



"""
we can perform different functions on multiple arrays
like addition subtraction etc.
"""
x = np.array([[1,2],[3,4],[5,6]])
y = np.array([[7,8],[9,10],[11,12]])

print("sum of x and y is:", x+y) # addition
print("subtraction of x and y is:", x-y) # subtraction
print("product of x and y is:", x*y) # multiplication
print("division of x and y is:", x/y) # division

# as the matrices of x and y are same i-e (3,2)(3,2) shape
# but dot product can only be performed when the number of columns
# in the first matrix must match the number of rows in the second matrix.
# i-e we need (3,2)(2,3)
# so for this we will transpose of y that will change the matrix of y from (3,2) into (2,3)
dot_product= x.dot(y.T)
print("dot product of x and y is:", dot_product)
# we cannot do these operation on python native lists

"""
1.Simple (element-wise) product multiplies corresponding elements of 
two arrays, resulting in an array of the same shape.

2.Dot product involves matrix multiplication, where the rows of the 
first matrix are multiplied by the columns of the second, producing 
a scalar (for vectors) or another matrix.

"""