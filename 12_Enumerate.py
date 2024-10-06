# The ‘enumerate’ function adds counter to an iterable and returns it.

# for i,item in list1:
# print(i,item) # Prints the items of list 1 with index

# for example, we have a list
l = [3,54,23,223]
index = 0
for item in l:
    print(f'the item number at index {index} is {item}')
    index +=1

# we can make this code easier by using enumerate function.

# example main
for index,item in enumerate(l):
    print(f'the item number at index {index} is {item}')

# the main example and the other example will print the same output
# so enumerate function make it much easier by writing only 2 lines of code.