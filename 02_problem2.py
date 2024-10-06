# Write a program to print third, fifth and seventh element from a list using enumerate
# function.
# method 1
list = [1,2,3,4,5,6,7,8]
for index,item  in enumerate(list):
    if index in [2,4,6]:
        print(f'the item at index {index} is {item}')

# method 2
list = [1,2,3,4,5,6,7,8]
for i,item in enumerate(list):
    if i == 2 or i == 4 or i ==6:
        print(f'the item at index {i} is { item }')