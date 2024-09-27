"""
in strings defining a function will create a whole new string because the main string cant be changed
but in List defining a function or method will not create a new list
"""

list = ["apple", "Banana","Pineapple", 23, 69.99, True]
list.append("Hassam") # append means at the end adding value
print(list)

# in strings
str = "Shaq, Ahmad, Khan"
a=str.replace("S","A")
print(str)
print(a)  # it's the main difference between lists and strings because here the main str is not changed, but we define a new string with name "a"

# other methods of lists

l1=[2,1,3,6,4,8,7]
l1.sort() # it will sort the whole list
print(l1)
l1.reverse() # it will reverse the whole list
print(l1)
l1.insert(8,-1) # insert -1 at index 8
print(l1)
l1.pop(1) # delete element at index 1
print(l1)
l1.append(9) # it will add an element at the end of the list
print(l1)
l1.remove(9) # it will remove 9 from the list, but we can remove value according to the list