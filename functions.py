#functions are nothing but a block of code that performs some specific task
#function: 1.add water/detergent 2.wash dishes 3.dry them
#Problem: you are given two list of numbers and you need to find total of each of these list
#tom_exp_list=[2100,3400,3500]
#john_exp_list=[200,500,700]
#total=0
#for item in tom_exp_list:
#    total=total+item
#print("Tom's total expenses:",total)
#total=0
#for item in john_exp_list:
#   total=total+item
#print("John's total expenses:",total)

#the code ive written here is on for loop and not a function
# and it will creat problems of length because for a hundred line of
# code we have to write 100 for loops so lets write func

def calculate_total(exp): #func argument
    total=0
    for item in exp:
        total=total+item
    return total #func return value   #whole is called func body
tom_exp_list=[2100,3400,3500]
john_exp_list=[200,500,700]

toms_total=calculate_total(tom_exp_list)
johns_total=calculate_total(john_exp_list)

print("toms total expense is:",toms_total)
print("johns total expense is:",johns_total)