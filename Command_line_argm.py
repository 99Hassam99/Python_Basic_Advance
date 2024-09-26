"""
command line argument processing using argparse

there are 2 types of arguments
1) positional arg
2) optional arg
"""
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number") #to make arg optional just add -- in front of a name
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation",help="operation",\
                        choices=['add','subtract','multiply'])

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1+n2
    elif args.operation == "subtract":
        result = n1-n2
    elif args.operation == "multiply":
        result = n1*n2
    #else:
     #   print("unsupported Operation")

    print("Result",result)

"""
here we are writing code that takes 3 inputs
1)first numb
2)second numb
3)operators(add sub etc)

it should return result of operation based on inputs
"""