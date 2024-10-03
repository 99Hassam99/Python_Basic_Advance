# Write a program to make a copy of a text file “this. txt”

with open("08_this.txt","r")as f:
    content=f.read()

with open("08_this_copy.txt","w")as f:
    f.write(content)