import sys
#Raise Exception
try:
    raise MemoryError ("Memory error")
except MemoryError as e:
    print(e)
"""
We are now creating user defined exception.
Exception is basically an instance/ object of a class 

User defined exception are always derived from Exception base class
"""
class Accident (Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("accident occured. Take detour")



try:
    raise Accident ("Crash")
except Accident as e:
    e.handle()
"""
Finally Statement
It something that people use to do cleanup
eg:
A function which is processing a file 
"""

def process_file():
    try:
        f=open("D:\\Python\\PyCharm Coding.txt")
        x=1/0
    except FileNotFoundError as e:
        print("Inside except")
    finally:
        print("Cleaning up file")
        f.close()
process_file()

# it will excecute by finally no matter what, even if there is an error.