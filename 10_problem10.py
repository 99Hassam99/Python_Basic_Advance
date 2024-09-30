# Write a program to print multiplication table of n using for loops in reversed
# order

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {11-i} = {number * (11-i)}")