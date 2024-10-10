"""
mom is handling 3 threads, cooking food, handling baby and holding phone so mom is doing multithreading

for a given list of numbers print square and cube of every number
for examples = [2,3,8,9]
"""

import  time
import  threading
from threading import Thread

def cal_square(number):
    print("Calculate square numbers.")
    for n in number:
        time.sleep(0.2)
        print('square',n*n)

def cal_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube",n*n*n)

arr = [2,3,8,9]

t=time.time()

t1 = threading.Thread(target = cal_square, args = (arr,))
t2 = threading.Thread(target = cal_cube, args = (arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in time:",time.time()-t )
print("hah..i am done with all my work.")