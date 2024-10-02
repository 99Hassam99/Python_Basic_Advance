# We can have a value as default argument in a function.
# If we specify ending = “Thanks” in the line containing def, this value is used when no
# argument is passed.


def greetings(name, ending="Thanks"): # in this func argmnt ending has a default value.
    print(f'Hello,{name} have a good day!')
    print(ending)
greetings("Hassam","How are you") # here default argument is not used because we did pass it a value
greetings("Ahmad") # here default argument is used because we did not pass it a value


# example 2
def greet(name = "stranger"):# function body
    print(name)
greet() # name will be "stranger" in function body (By default)
greet("Syed_Pro22") # name will be "harry" in function body (passed value, No default argmnt used)

