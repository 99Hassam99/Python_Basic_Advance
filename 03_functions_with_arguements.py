# A function can accept some value it can work with. We can put these values in the
# parentheses.

# name and ending are parameters that are passed as an argument to a function
def good_Day(name, ending): # in this function we pass an argument like good_Day(argument)
    print("Good Day, "+name) # "+" concatenation
    print(ending)

good_Day("Shaq","Thank You")
good_Day("Hassam","Thanks")

# example 2
# we can also use a return value statement
def greet(name):
    print("Hello, "+name)
    return "Thanks!" # so to make an output for print(a,b, upto so on) return statement is must

a=greet("Jaani") # if we put a before function {greet()} without returning it will give a None value.
print(a)
b=greet("Janan")
print(b)