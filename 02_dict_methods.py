d={} # empty dictionary
marks = {
    "Hassam":87, # "" is "Key",  87 is key value
    "Salman":91,
    "Uzair":84,
    "Obaid":60,
    0:"Shaq" # we can assign int to the key
}
print(len(marks)) # print length of dictionary
print(marks.items()) # it gives the result in tuple "()" form
print(marks.values()) # it gives the values
print(marks.keys()) # it gives the keys

print(marks) # here Hassam has 87 marks
marks.update({"Hassam":93, "Ahmad":92}) # it can be changed as dict are mutable or changeable
print(marks) # here hassam marks are updated to 93, and also add a new key to the dictionary with the name Ahmad

# both will return the value of Hassam but
print(marks.get("Hassam"))
print(marks["Hassam"])

# the difference arises when we don't know about the name, and we want to check it,
# there if the key name is wrong the ".get" method will return "None" while the simple index method will return an error
# for example
print(marks.get("Hassam2")) # it returns none
# print(marks["Hassam2"]) # it return an error


# Removes the specified key and returns its value. If the
# key is not found, the default value is returned.
print(marks.pop(0)) # return 0 key value
print(marks) # the 0 "Key" is removed

# Removes all items from the dictionary.
# marks.clear()
# print(marks)

print(marks.setdefault('Ali', 25)) # it will add this new key to dic
# print(marks)

# Returns a shallow copy of the dictionary.
copy_dict=marks.copy()
print(copy_dict)



#  Creates a new dictionary from the given iterable with specified values.
new_dic = marks.fromkeys(marks, "unknown")
print(new_dic)

# popitem method removes the last key from dictionary
items = marks.popitem()
print(items)
print(marks)