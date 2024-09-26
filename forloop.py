#Problem:store monthly expenses in a list and find out total expenses for all months using for loop

exp=[2340,2500,2100,3100,2980]
#total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]

total=0
for item in exp:
    total=total+item
print(total)
