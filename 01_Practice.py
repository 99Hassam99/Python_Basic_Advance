# Create any multithreaded code using for loop for creating multithreads
# for i in range(10):
#     th = Thread(target=func_name, args=(i,))
# print total active threads in multithreaded code using threading.active_count()
import time
import threading
from threading import Thread

def sleeping(i):
    print("Thread %i will sleep."% i)
    time.sleep(5)
    print("Thread %i will sleep."% i)

for i in range(10):
    th = Thread(target=sleeping,args=(i, ))
    th.start()
    print("current Threads: %i."% threading.active_count())