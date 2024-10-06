def Func():
    print("The function")
Func()

if __name__ == "__main__":
# this code is directly executed by running the file present in it
    print(" we are directly running this code")
    Func()
    print(__name__)

# now this code will print name only if the __name__ == __main__ and if there is any link file
# with the help of this code that code will not be able to print this code name.