# if-elif-else ladder


marks=int(input("Enter your Marks: "))

if(marks>=90):
    print("Grade A+.")

elif(marks>=80):
    print("Grade A.")


elif(marks>=70):
    print("Grade B.")


elif(marks>=60):
    print("Grade C.")

else:
    print("You are failed")

print("End of code")


# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18

age = int(input("Enter your age: "))
if(age >= 18):
    print("Yes.")
