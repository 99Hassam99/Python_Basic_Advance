# List Set Dict Comprehensions

# 1. Create a Dictionary which contains the Binary values mapping with numbers found
# in the below integer and binary, and save it in binary_dict.
# Example :
#
#     integer = [0, 1, 2, 3, 4]
#     binary = ["0", "1", "10", "11", "100"]
#     binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

# 2. Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
# a + i = 0
# Example:
#
# integer = [1, -1, 2, 3, 5, 0, -7]
# additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

# 3. Create a set which only contains unique sqaures from a given a integer list.
# integer = [1, -1, 2, -2, 3, -3]
# sq_set = {1, 4, 9}

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

z = zip(binary,integer)
binary_dict={integer: binary for integer, binary in z}
print(binary_dict)

# list
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integer]
print(additive_inverse)

# set
integer=[1, -1, 2, -2, 3, -3]
sq_set={i*i for i in integer}
print(sq_set)