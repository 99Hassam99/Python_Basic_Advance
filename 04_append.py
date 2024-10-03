"""
MODES OF OPENING A FILE
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.
"""

"""
append means adding some value at the end
"""

strg =", What are you doing!"

f=open("02_write_my_File.txt","a")
f.write(strg)
f.close()