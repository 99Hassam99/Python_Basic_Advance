# Write a program to accept marks of 6 students and display them in a sorted manner.

student_marks_list =  []

m1 = int(input("Enter marks of student: "))
student_marks_list.append(m1)
m2 = int(input("Enter marks of student: "))
student_marks_list.append(m2)
m3 = int(input("Enter marks of student: "))
student_marks_list.append(m3)
m4 = int(input("Enter marks of student: "))
student_marks_list.append(m4)
m5 = int(input("Enter marks of student: "))
student_marks_list.append(m5)
m6 = int(input("Enter marks of student: "))
student_marks_list.append(m6)
student_marks_list.sort()
print(student_marks_list)

# we change it to integer because list elements are string by default
# so if we sort the default list it will be sorted in alphabetical order
# that's why we changed it to integer, that's how it's sorted in digits order