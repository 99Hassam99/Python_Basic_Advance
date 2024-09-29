# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter username: ")

words = len(username)

if(words<10):
    print("Characters are less than 10")
else:
    print("Characters are not less than 10")


# or we can also write it as

username = input("Enter username: ")
if(len(username)<10):
    print("Characters are less than 10")
else:
    print("Characters are not less than 10")
