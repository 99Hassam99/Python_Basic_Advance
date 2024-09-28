s = {1,2,3,2,4,3,2,4,1,"Shaq"} # we can add strings to a set
print(s,type(s))

s.add(599) # it will add new element in the set
s.add("ahmad")
print(s,type(s))

# sets are unordered
# sets are not indexed means cannot access elements by index
# sets items are immutable
# sets do not have duplicate items

print("length of set:" , len(s))

#  Updates the set s and removes 1 from s.
s.remove(1) # it removed 1
print(s)

# Removes an arbitrary element from the set and return the element removed.
s.pop()
print(s)

# empties the set s
s.clear()
print(s)