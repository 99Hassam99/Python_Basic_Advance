# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word "twinkle"
from time import perf_counter

f=open("01_poems.txt", "r")
data = f.read()
if("twinkle" in data):
    print("The word is present in data")
else:
    print("The word is not present in data")

f.close()


# example on with statement

with open("01_poems.txt") as f:
    data=f.read()
    if("twinkly" in data):
        print("The word twinkle is present in data")
    else:
        print("The word twinkle is not present in data")
