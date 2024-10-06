# Store the multiplication tables generated in problem 3 in a file named Tables.txt

# problem 3
n = int(input("Enter a number: "))
table = [n*i for i in range(1,11) ]
with open("1.txt","a") as f:
    f.write(f"table of {n}: {str(table)} + \n")