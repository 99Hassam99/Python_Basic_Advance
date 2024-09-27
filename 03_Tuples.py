# we need some data type that can be collection as well as immutable so it is tuple

# lets create a tuple

a = () # tuple
print(type(a))

# keep in mind that if we assign a single value to it then python will consider it as an int for example

a = (1) # int
print(type(a))

# so for that we should assign a (comma){ , } with 1

a = ( 1, ) # tuple
print(type(a))


a = ( 1,233,234,544,False,"String" ) # still a tuple
print(type(a))

# we cant change elements in tuples by indexing it will give an error
# a[0] = 2
# print(a)

# tuples are immutable like strings


