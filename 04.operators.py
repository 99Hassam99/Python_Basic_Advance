# arithmatic operators
# 7 + 4 = 11
# 7 and 4 are operands and + is operator and 11 is called result
# eg

a = 7
b = 4
c = a+b
d = a-b
e = a*b
f = a/b
print(c,d,e,f)


# assignment operators
# a = 1
# a += 1
# a -= 1
a = 4-2 # assign 4-2 in a with = sign
print(a)
b = 6
b += 3 # pre increment operator, it increment b by 3 so the new value will be 9
print(b)
c = 6
c -= 3  # pre decrement operator, it decrement c by 3 so the new value will be 3
print(c)
e = 3
e *= 3
print(e)
r=4
r /= 2
print(r)

# comparison operators
r = 1==1
print(r)
z = a==a
print(z)
c = a != a
print(c)
t = a < a
print(t)
g = a > a
print(g)
d = a <= a
print(d)
f = a >= c
print(f)
# the return value of comparison operator is always a boolean value


# Logical operator

e = True or False
# truth table for "Or" operator
print("True or False is:", True or False )
print("True or True is:", True or True )
print("False or True is:", False or True )
print("False or False is:", False or False )


e = True and True
# truth table for "And" operator
print("True and False is:", True and False )
print("True and True is:", True and True )
print("False and True is:", False and True )
print("False and False is:", False and False )


# Not operator make the true false and false to true
print(not (True))
