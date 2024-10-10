"""
create two processes,
1. first is to calculate squares of all numbers.
2. second is to calculate cubes of all numbers.
"""

import time
import multiprocessing


square_result=[]
cube_result=[]
def cal_square(numbers):
    global square_result
    for n in numbers:
        # time.sleep(2)
        print("squares"+str(n*n))
        square_result.append(n*n)
    print("within a process:Result"+str(square_result))

def cal_cube(numbers):
    global cube_result
    for n in numbers:
        # time.sleep(2)
        print("cubes"+str(n*n*n))
        cube_result.append(n*n*n)
    print("within a process:Result"+str(cube_result))

if __name__ == "__main__":
    arr = [2,3,8,9]
    p1= multiprocessing.Process(target=cal_square,args=(arr,))
    p2= multiprocessing.Process(target=cal_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("result."+str(square_result))
    print("result."+str(cube_result))


    print("done: ")