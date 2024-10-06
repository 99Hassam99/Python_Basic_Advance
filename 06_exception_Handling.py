# exception handling
# There are many built-in exceptions which are raised in python when something goes
# wrong.
# Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause.

# try:
# # Code which might throw exception
# except Exception as e:
# print(e)

# When the exception is handled, the code flow continues without program interruption.
# We can also specify the exception to catch like below:

# try:
# # Code
# except ZeroDivisionError:
# # Code
# except TypeError:
# # Code
# except:
# # Code # All other exceptions are handled here.

# this is a correct code but what if a user write a string in an ouput, then it will raise an error
# which should be handle by giving some message like "invalid number" instead of an error
"""
a=int(input("hey,write a number:"))
print(a)
"""

# lets try to remove exception

try:
    a=int(input("Hey! Enter a number: "))
    print(a)
except Exception as e:
    print(e)
print("Thank You!")



try:
    a= int(input("Enter: "))
    print(a)

except TypeError as t:
    print(t)
except Exception as e:
    print(e)
except ZeroDivisionError as d:
    print(d)

