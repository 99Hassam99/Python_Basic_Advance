# We can also use f.readline() function to read one full line at a time.
# EXAMPLE 1
f = open("01_file.txt","r")

lines=f.readlines() # it will print all the lines

print(lines,type(lines))

f.close()

# EXAMPLE 2
"""
line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

line4=f.readline()
print(line4,type(line4))
"""

# EXAMPLE 3
# we can also perform this function through while loop
# line=f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
#
# f.close()


