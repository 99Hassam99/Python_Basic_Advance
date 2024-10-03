"""
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.

Python has an open() function for opening files. It takes 2 parameters: filename and
mode.

In order to write to a file, we first open it in write or append mode after which, we use
the python’s f.write() method to write to the file!
"""

strg ="Hey Shaq, You are amazing!"

f=open("02_write_my_File.txt","w")
f.write(strg)
f.close()