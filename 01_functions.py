# difference between a function and a normal code
# a= int(input("Enter a number: "))
# b= int(input("Enter a number: "))
# c= int(input("Enter a number: "))
# average=(a+b+c)/3
# print(average)
# without a function we have to define a code every time we need it but with function we can make
# it easy by just defining function for one time and executing it for 100 times.
# a= int(input("Enter a number: "))
# b= int(input("Enter a number: "))
# c= int(input("Enter a number: "))
# average=(a+b+c)/3
# print(average)

# A function is a group of statements performing a specific task.
# When a program gets bigger in-size and its complexity grows, it gets difficult for a
# program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of

# syntax
# def func1():
#     print('hello')
# func1() # it will execute the function

# it's function body or definition
# The part containing the exact set of instructions which are executed during the function
# call.
def average():
    a= int(input("Enter a number: "))
    b= int(input("Enter a number: "))
    c= int(input("Enter a number: "))
    averge=(a+b+c)/3
    print(averge)
average()  # it's called the function call
print("Your average")
average() # Whenever we want to call a function, we put the name of the function followed by parentheses
average()
"""
it's the difference like we have seen earlier 
that for this type of code, we write that input function
for 3 times but in function we just write it onces which make it unique and easier for us.
"""