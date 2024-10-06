# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
# the exception.


# finally will run even if there is an exception or the code runs successfully but
# it's mainly used in a function.

# for example
try:
    a = int(input("enter"))
    print(a)
except Exception as e:
    print(e)
finally:
    print("you are in finally") # output: 12. you are in finally


# this is without function example here the [print("you are in finally")] if we use finally or not
try:
    a = int(input("enter"))
    print(a)
except Exception as e:
    print(e)

print("you are in finally") # output: invalid literal for int() with base 10: 'qwqw'.. you are in finally


# like this
# but the difference lies when we use a fun, so for example
def main():
    try:
        a=int(input("Enter: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("you are in finally")
main()  # OUTPUT: 12.....you are in finally


# here it will run { print("you are in finally") } with keyword FINALLY but if we donot use the word FINAlly
# then it will not use { print("you are in finally") }
def main():
    try:
        a=int(input("Enter: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    print("you are in finally")

main() #OUTPUT : invalid literal for int() with base 10: 'qw'

# see the last one did not print it
