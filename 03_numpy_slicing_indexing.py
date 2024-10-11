"""
numpy - slicing/stacking arrays, indexing with boolean arrays

Topics:
1. Indexing and slicing
2. iterating through arrays
3. Stacking together 2 arrays
4. Indexing with boolean arrays
"""
import numpy as np

# similarities between numpy and python list indexing

# example of python indexing
py_list = [7,8,9] # index 0 = 7 , index 1 = 8 , index 2 = 9
ind_list = py_list[0:2] # print index 0 and 1 and leave index 2
print(ind_list)

# example of numpy array list indexing
# one dimensional
np_list = np.array([7,8,9]) # index 0 = 7 , index 1 = 8 , index 2 = 9
ind_lis = np_list[0:2] # print index 0 and 1 and leave index 2
print(ind_lis)

# two dimensional
np_list = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(np_list)
print(np_list[1,2]) # here 1 is row and 2 is the index
"""
0st row
[6       7     8]
1st row 
[1       2     3] # index 0=1, 1=2, 2=3 so [1,2] means row 1 and 2nd index
2nd row
[9       3     2]
"""
print(np_list[0:2,2])
"""
# [0:2] means 0 row and 1st row 
# [0:2,2] and 2 means index 2
0st row
[6       7     8]
1st row 
[1       2     3] # index 0=1, index 1=2, index 2=3 
2nd row
[9       3     2]
np_list[0:2,2]
it means that in row 0 and 1 select index 2 numbers in both rows
it prints [8,3]
"""

print("last element(-1):",np_list[-1]) # -1 means the last element in the list

print("last row+2columns index:",np_list[-1,0:2]) # -1 means last row and 0:2 means column index from 0:2 so it print last row 1st 2 elements

print("all rows and 1-2index columns: ",np_list[: , 1:3]) # (:) go through all the rows and (1:3) means print index 1 and 2 elements of all the rows


for row in np_list:
    print("for:",row)
# for loop use will print the list individually

for cell in np_list.flat: # making the entire list flat row wise
    print("flat:",cell)

a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
print("a list:\n:",a)
print("b list:\n:",b)

# consider a and b are two boxes and if we join them we can write it as
c =np.vstack((a,b)) # it joins the 2 boxes vertically
print("Boxes Joined:\n",c)

c =np.hstack((a,b)) # it joins the 2 boxes horizontally
print("Boxes Joined:\n",c)



x = np.arange(30).reshape(2,15)
print("long list",x)
y = np.hsplit(x,3) # divides the long list in 3 list
print("hotizontally:\n",y)
print(y[0])
print(y[1])
print(y[2])

y =np.vsplit(x,2)
print("vertically:\n",y)

ind_bool_arr=np.arange(12).reshape(3,4)
print("indexing with boolean array-list:\n",ind_bool_arr)
comp_bool = ind_bool_arr > 4
print(comp_bool)

print(ind_bool_arr[comp_bool]) # it will print the true values

ind_bool_arr[comp_bool]=-1
print(ind_bool_arr) # it will simply replace the true elements with -1