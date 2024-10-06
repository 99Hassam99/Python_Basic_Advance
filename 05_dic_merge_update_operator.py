# New operators | and |= allow for merging and updating dictionaries.
from heapq import merge

dic1 = {"a":1 , "b":2}
dic2 = {"c":3 , "d":4}
merged = dic1 | dic2
print(merged)

dict3 = {"age": 23 , "salary": 23000}
dict4 = {"name":"Hassam",
    "Occupation":"Student",
    "Phone No.":+923130422253,
     }
merged = dict4 | dict3
print(merged)

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager

# method 1
with (
    open(("file1.txt"),"r") as f1,
    open("file2.txt","r") as f2
):
    print(f1.read(),f2.read())

# method 2
with open("file1.txt") as f1 , open("file2.txt") as f2:
    content1 = f1.read()
    content2 = f2.read()
    print(content1,content2)
    