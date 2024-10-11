"""
numpy's most useful feature is the n dimensional array object (i-e ndarray)

NumPy is the fundamental package for scientific computing in Python.
It is a Python library that provides a multidimensional array object,
various derived objects (such as masked arrays and matrices), and an
assortment of routines for fast operations on arrays, including mathematical,
logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms,
basic linear algebra, basic statistical operations, random simulation and much more.
-> syntax:

import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6]])
a.shape
(2, 3)


we have a python list then why use numpy array
there are 3 main benefits of using numpy array
1.Less memory
2.fast
3.convenient
"""

import numpy as np
import time
import sys

# reason 1 less memory
l = range(1000)
print(f'{sys.getsizeof(1)*len(l)} : bites') # python list are heavy | output = 28000 bites consumed

aray = np.arange(1000)
print(f"{aray.size*aray.itemsize}: bites") # whereas numpy list are light | output 8000 bites consumed

# reason 2 Fast and convenient
size = 100000
l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)
# python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print(f"Python list took time: {(time.time()-start)*1000} milliseconds")
# numpy array
start = time.time()
result =a1+a2
print(f"Numpy array took time: {(time.time()-start)*1000} milliseconds")


# numpy is 9X times faster than python list