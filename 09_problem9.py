# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

s[1,2]=1
print(s)

# there are 2 errors in this

# list cant be included in a set
# sets are immutable and hashable, that is they cant be changed
# while lists are mutable and unhashable
