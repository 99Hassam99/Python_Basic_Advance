#  Write a program to find out whether a given post is talking about “Harry” or not.

post = "Hey Hassam, How are you How old are you Hassam"
# we can also use input() func for this like:
post = input("Enter a post: ")

if("Hassam".lower() in post.lower()):
    print("This post is talking about Hassam.")
else:
    print("This post is not talking about Hassam.")