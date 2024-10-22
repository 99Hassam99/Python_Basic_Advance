# Commandline Argument Processing using argparse
# Take subject marks as command line arguments
# example:
#     python3 cmd.py --physics 60 --chemistry 70 --maths 90
# Find average marks for the three subjects using command line input of marks.

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--physics',help='physics marks')
    parser.add_argument('--chemistry',help='chemistry marks')
    parser.add_argument('--biology',help='biology marks')

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.biology)

    print('Result:',(
        int(args.physics) + int(args.chemistry) + int(args.biology)
    )/3)

    # python3 cmd.py --physics 60 --chemistry 70 --maths 90