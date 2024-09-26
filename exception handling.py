# exceptions are errors detected at the time of program execution
"""
1/0 ....1 is not divisble by 0,its an exception
"a.b.c"+2 , concatening string with int

how to handle exception lets do it
"""
x=input("Enter No.1:")
y=input("Enter No.1:")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception:")
    z=None
print("Division is:",z)


"""
try:
    while road_is_clear():
         drive()
except Accident as e:
         take_detour()
"""