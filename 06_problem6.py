# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
from tkinter.font import names

# emp_dic={}
#
# name1 = input("Enter name1: ")
# lang1 = input(f"Enter{name1}'s favourite language: ")
# emp_dic[name1]=lang1
#
# name2 = input("Enter name2: ")
# lang2 = input(f"Enter{name2}'s favourite language: ")
# emp_dic[name2]=lang2
#
# name3 = input("Enter name3: ")
# lang3 = input(f"Enter{name3}'s favourite language: ")
# emp_dic[name3]=lang3
#
# name4 = input("Enter name4: ")
# lang4 = input(f"Enter{name4}'s favourite language: ")
# emp_dic[name4]=lang4
#
# print("\n Favoutite language of 4 friends are: ")
# print(emp_dic)



d = {}
name= input("Enter your name: ")
lang=input("Enter your fvrt language: ")
d.update({name:lang})

name= input("Enter your name: ")
lang=input("Enter your fvrt language: ")
d.update({name:lang})

name= input("Enter your name: ")
lang=input("Enter your fvrt language: ")
d.update({name:lang})

name= input("Enter your name: ")
lang=input("Enter your fvrt language: ")
d.update({name:lang})

print(d)