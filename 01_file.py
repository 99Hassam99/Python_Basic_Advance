"""
File I/O
The random-access memory is volatile(Temporary), and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it

# reading a file
f = open("01_file.txt", "r") # r is by default means read, if we write it or not
data = f.read()
print(data)
f.close()
"""

# writing a file
f = open("01_file.txt", "r") # r is by default means read, if we write it or not
data = f.read()
print(data)
f.close()

# read and write file are 2 of the most important work on file I/O