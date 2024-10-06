# List Comprehension is an elegant way to create lists based on existing lists.
# list1 = [1,7,12,11,22,]
# list2 = [i for item in list 1 if item > 8]

# for example, we have a list
l = [2,3,4,5,6,7,8,9]
squared_list=[]

for item in l:
    squared_list.append(item*item)

print(squared_list)

# it's a tough process

# we can make it easier by using list comprehension method

# for example
myList=[2,3,4,5,6,7,8,9]
squared_lists = [ i*i for  i in myList]
print(squared_lists)

# see with the help of list comprehension we make that 5 6 lines of code easier by just writing 3 lines of code.
