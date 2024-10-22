# create any set anf try to use frozenset(setname)
#
# Find the elements in a given set that are not in another set
#
#     set1 = {1,2,3,4,5}
#     set2 = {4,5,6,7,8}
#
#     diffrence between set1 and set2 is {1,2,3}

list=[]
dict ={}
tuple=()
set={2}
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print('Original set')
print(set1)
print(set2)

print('difference between set1 and set2 using difference()')
print(set1.difference(set2))

print('difference between set2 and set1 using difference()')
print(set2.difference(set1))

print('difference between set1 and set2 using - operator')
print(set1 - set2)


print('difference between set2 and set1 using - operator')
print(set2 - set1)