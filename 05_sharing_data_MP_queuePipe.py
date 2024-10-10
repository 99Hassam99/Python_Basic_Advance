"""
MP Queue vs Queue
MP Queue live in shared memory while queue lives in a process memory.
MP Queue is used to share data bw processes while queue is used to shared data between threads
"""

import multiprocessing

def cal_square(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__ == "__main__":
    numbers = [1,2,4]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())