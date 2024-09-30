# Write a program to find whether a given number is prime or not.

number = int(input("Enter a number: "))
for i in range(2, number):
    if (number%i)==0:
        print("The number is not prime")
        break
else:
    print("The number is prime")
