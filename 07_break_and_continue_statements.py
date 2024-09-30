# break statement
# ‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now.
from tkinter.scrolledtext import example

for i in range(40):
    if(i == 35):
        break # it will exit the loop when reachedat this iteration "35"
    print(i)

# example
for i in range(0,80):
    print(i)
    if i == 3:
        break

# continue statement
# ‘continue’ is used to stop the current iteration of the loop and continue with the next
# one. It instructs the Program to “skip this iteration”.

for i in range(40):
    if(i==35):
        continue # it will skip this "35" iteration
    print(i)

# example

for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
       continue
    print(i)
