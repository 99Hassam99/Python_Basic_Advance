# The best way to open and close the file automatically is the with statement.

f = open("02_write_my_File.txt")
print(f.read())
f.close()

# the same method can be done using "With" statement like this:
# where no close statement is needed because close statement is heavy

with open("02_write_my_File.txt") as f:  # it's like a tool that automatically closes the file
    print(f.read())

# you don't have to explicitly close the file