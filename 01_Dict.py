# understanding the difference between str, list, tuple, dict
a="" # string
b=[] # list
c=() # tuple
d={} # dictionaries
e={1,2}# sets, both sets and dic uses curly "{}" brackets
e=set() # empty set
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# let's have a look on dictionaries
# dict are the collection of key value pairs
marks = {
    "Hassam":87,
    "Salman":91,
    "Uzair":84,
    "Obaid":60
}
print("Marks are:", marks ," Type is: ", type(marks))

# it indexed but not like 0,1,2,3: it indexed by its name
# so for that

print(marks["Hassam"]) # it will tell the marks of Hassam
# print(marks[0]) | "it will give an error because it cannot be indexed by digits"




# example 2

a={
    "Key":"Value",
    "Shaq":"Code",
    "Marks":"94",
    "list":[1,2,3,4]
}
print(a)
print(a["Key"])
print(a["list"])