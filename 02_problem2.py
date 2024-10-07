# Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# " The name of the student is Harry, his marks are 72 and phone number is 99999888 "

name = input("Enter a name: ")
marks = int(input("enter marks: "))
phone_no = int(input("Enter your phone no: "))

s = "The name of the student is {}, his marks are {} and phone number is {} ".format(name,marks,phone_no)
print(s)