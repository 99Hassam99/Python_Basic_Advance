# pass is a null statement in python.
# It instructs to “do nothing”.
# sometimes we write 2 loops, but we want to work on the 2nd loop and laterally work on 1st
# but if we do that it will give an error.
# for example

for i in range(4):
    pass # it allows us to work on while loop and leaving for loop for later work, without pass statement it gives an error

i=0
while(i<45):
    print(i)
    i +=1