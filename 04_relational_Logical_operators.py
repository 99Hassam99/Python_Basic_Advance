# Relational Operators are used to evaluate conditions inside the if statements. Some
# examples of relational operators are:
# ==: equals.
# > =: greater than/ equal to.
# < =: lesser than/ equal to.

age= int(input("Enter Your age"))

if ( age>=18):
    print("you are adult. ")
elif(age <= 17):
    print("you are underage. ")
elif(age >= 0):
    print("You are not adult. ")
else:
    print("You are not born.")

print("End of code")


# in this code the else statement  { else: print("You are not born.")} is not reachable because of:
# the conflicting elif statements. to address this issue we use  Logical operators.


# In python logical operators operate on conditional statements. For Example:
# • and – true if both operands are true else false.
# • or – true if at least one operand is true or else false.
# • not – inverts true to false & false to true.

age= int(input("Enter Your age"))

if ( age>=18):
    print("you are adult. ")
elif(age > 0 and age < 18): # now it will allow the end else statement to be executed if someone type 0 or -1
    print("you are underage. ")
else:
    print("You are not born.")

print("End of code")