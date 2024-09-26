total=0 #global vs local variables
def sum(a,b=0): #default argument

    """
    //documentation strings
    this func takes 2 arguments which are integ no. and it will return sum
    of them as an output
    """
    print("a:", a)
    print("b:", b)

    total=a+b
    print("total inside func:",total)
    return total

n=sum(40,32)
print('total outside function:',total)

#arguments are of two types
#positional
#named
#default arguments