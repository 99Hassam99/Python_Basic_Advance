b = (1,4,22,22,22,22,22,22,22,22,22,22,3,43834,23.22,False,"String")

print(b)
print(type(b))

# methods or functions
no= b.count(22) # it counts the number of same element in the list
print(no)

# in tuples new tuples will be returned because of immutable

i=b.index(4) # it takes the value from tuple list and return its index value
print(i)

a=len(b) # it will tell the length of tuple like the total number of elements in the list
print(a)


s = (1,2,3,4)
c=max(s) # it will return the max value in the list
print(c)

s = (1,2,3,4)
c=min(s) # it will return the min value in the list
print(c)


s = (1,2,3,4)
c=sum(s) # it will add all the int values in the tuple list
print(c) # returns 10 / 1+2=3+3=6+4=10



list=[1,2,3,4]
my_tuple=tuple(list) # it will convert a list into a tuple
print(my_tuple)

repeated = my_tuple*3 # it will repeat the list for 3 times
print(repeated)

# membership, it means checking an element in a list
print(2 in my_tuple)
print(5 in my_tuple)

new_tuple = (1,3,5,7,9)
sliced = new_tuple[1:4] # same as all others slicing
print(sliced)

# unpacking
a,b,c,d,e = new_tuple # giving each element of a tuple a new variable
print(a,b,c,d,e)


