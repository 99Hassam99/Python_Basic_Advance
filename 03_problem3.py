# Write a program to detect double space in a string.

name = "My name is  hassam."
print(name.index(" "))
print(name.find("  ")) # it gives 10 value because the doble spaces are at index 10, starting the line from 0 position and it detect it on index 10
