# ‘global’ keyword is used to modify the variable outside the current scope.
# 1
a = 89 # global variable. It's those variable that we can use inside the function as well as outside  the functon.

def func():
    a = 3 # local variable of this function
    print(a) # it print 3

func()
print(a) # it print 89

# but if we use a global keyword inside a function then,
# 2
b = 90
def gl_vr():
    global b # it will change the global variable value to the function value because global variable is now used inside a function
    b=3
    print(b) # prints 3

gl_vr()
print(b) # prints 3 ... value changed from 90 to 3

# functions variable are local means they can be use only inside a function