#in our monthy expense example,print month number and expense and then in the end print total expense

exp=[2340,2500,2100,3100,2980]
total=0
for i in range(len(exp)): #for i in range(0,5)
    print('Month;',(i+1),'Expense:',exp[i])
    total=total+exp[i]

    print('My Total Expense is:',total)