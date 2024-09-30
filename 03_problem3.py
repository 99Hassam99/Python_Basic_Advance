# Attempt problem 1 using while loop.

# Write a program to print multiplication table of a given number using for loop.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")

number = int(input("Enter a number: "))
i=1 # starts with 1
while(i<11):
    print(f"{number}*{i} = {number* i}")
    i +=1