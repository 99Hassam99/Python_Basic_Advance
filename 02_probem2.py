# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1 = int(input("Enter marks of subject1: "))
marks2 = int(input("Enter marks of subject2: "))
marks3 = int(input("Enter marks of subject3: "))

total_marks=marks1+marks2+marks3
percent_age=(total_marks/300)*100

if(percent_age >= 40 and marks1 >=33 and marks2>=33 and marks3>=33):
    print("You are passed",percent_age)
else:
    print("You are fail",percent_age)