# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("Enter a number: "))
for i in range(1,n+1):
    # print(""* (n-i),end="") it can be done like this
    # print("*"* (2*i-i), end="")
    # but can also be done like this
    print("*"*i,end="")
    print("")