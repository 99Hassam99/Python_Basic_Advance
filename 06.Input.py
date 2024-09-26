name = input("Enter name of user: ")
age = input("Enter age of user: ")
roll_no = input("Enter Roll No.: ")
semester = input("Enter semester: ")
section = input("Enter Section: ")
a = int(input("Marks of paper 1: "))
b = int(input("Marks of paper 2: "))
c = int(input("Marks of paper 3: "))
d = int(input("Marks of paper 4: "))

print("Name of user is: ", name)
print("Age of user is: ", age)
print("roll No of user is: ", roll_no)
print("semester of user is: ", semester)
print("section of user is: ", section)
print("Marks of paper 1 is : ", a)
print("Marks of paper 2 is : ", b)
print("Marks of paper 3 is : ", c)
print("Marks of paper 4 is : ", d)
total = a+b+c+d
print("Total marks :", total)
percentage = total*100/400
print("Percentage: ", percentage )

if percentage >=80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
else:
    print("Failed")