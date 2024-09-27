# 5. Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)
# func for counting  same elements in a tuple
countd_tuple = a.count(0)

print(f"number of zeros in tuple are: {countd_tuple}") # return 3 because there are 3 zeros in the list


# it can also be done like that
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))