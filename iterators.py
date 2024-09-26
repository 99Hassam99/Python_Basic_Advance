"""
what are iterators.
The process of going through elements of an array or list one by one
is called iterating through a loop, internally python uses a built-in function
called ITER
Iterators implementations using class
"""
a=["hey",'bro','snga','e']
for i in a:
    print(i)
itr=iter(a)
print(itr)
"""
for idle shell t iterate it one by one
next(itr)
hey
next(itr)
bro
next(itr)
snga
next(itr)
e
dir(itr)
there is a reverse function available lets check
a = ['a','b']
itr=reversed(a)
next(itr)
b
next(itr)
a
"""

#other examples
for element in [1,2,3]: #iterating through list
    print(element)
for element in (1,2,3): #iterating through tuple
    print(element)
for key in {'one':1,'two':2}: #iterating through dictionary keys
    print(key)
for char in "123": #iterating through all characters in a sring
    print(char)
for line in open("myfile.txt"): #iterating through every line in a file
    print(line,end='')
