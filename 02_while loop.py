i=1
while(i<6):
    print(i)
    i += 1

# In while loops, the condition is checked first. If it evaluates to true, the body of the loop
# is executed otherwise not!
# If the loop is entered, the process of [condition check & execution] is continued until
# the condition becomes False.
# one important thing about while loop is that we must have to make a condition false after sometimes otherwise it will become an infinite loop.

# Quick Quiz: Write a program to print 1 to 50 using a while loop.

c=1
while(c<51):
    print(c)
    c += 1

# example

a=0
while(a<5):
    print("Shaq")
    a = a+1 # same as a += 1
#Note: If the condition never become false, the loop keeps getting executed.
