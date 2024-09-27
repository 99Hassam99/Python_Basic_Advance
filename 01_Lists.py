"""
as we have studied that strings are immutable like if we want to change a character in a string it will give error
for example
a="Shaq"
print(a[0]) # it will print 0 index of "a" but if we want to change a character like
print(a[0]="y") # it will raise an error

but we can do it in "Lists"
"""

# Lists are containers to store a set of values of any data type
list = ["apple", "Banana","Pineapple", 23, 69.99, True]

print(list)
print(list[0])
list[0]='shaq'  #unlike strings "List" are mutable | it will change the 0 index value
print(list[0])
print(list)

# list vs strings
# in list value can be change while in strings it cant be changed
# similarities are that both have indexes
# for examples

print(list[1:4]) # it will store index 1-3 and ignore index 4