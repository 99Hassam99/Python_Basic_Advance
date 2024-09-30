# Write a program to print multiplication table of a given number using for loop.

# for i in range(0,11):
#     print(f"2*{i}",i)
#     i = i*2    | wrong attempt

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
