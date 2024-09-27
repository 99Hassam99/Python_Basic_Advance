# Check that a tuple type cannot be changed in python

a = (1,3,5,"Shaq")
a[3] = "4" # it wil give error because tuples are immutable that's they cant be changed
print(a)
