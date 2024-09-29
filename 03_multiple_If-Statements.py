# multiple if statments

marks=int(input("Enter your Marks: "))

# if statement 1
if(marks %2 == 0):
    print("Marks are even")
else:
    print("Marks are not even")
# end of if statement 1

# if statement 2
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
# end of if statement 2
print("End of code")

