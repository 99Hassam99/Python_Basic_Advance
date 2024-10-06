# WALRUS OPERATOR
# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to
# variables as part of an expression. This operator, named for its resemblance to the eyes
# and tusks of a walrus, is officially called the "assignment expression."

# # Using walrus operator
if (n := len([1,2,3,4,5,6]))>3:
    print(f'list is too long ({n} element, expected <=3)')
# # Output: List is too long (5 elements, expected <= 3)
# In this example, n is assigned the value of len([1, 2, 3, 4, 5]) and then used in
# the comparison within the if statement