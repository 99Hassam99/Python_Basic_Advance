"""
Generator is a simple way of creating iterators
"""


def remote_control_next():
    yield "cnn"
    yield "espn"
    yield "Geo"
    yield "Star"

itr=remote_control_next()
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))#when using python idle shell we can use alt+P coomand to rewind the last line

for c in remote_control_next():
    print(c)


"""
Fibonacci sequence
0,1,1,2,3,5,8,13,21,34,55....
its basically a sequence of numbers in which 
we basically keep on adding initial/first two numbers
to get the third number

eg:
we are going to produce fibonacci sequence using generators.
"""


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for f in fib():
    if f > 60:
        break
    print(f)

"""
Benefits of using generators over class based iterators,
1) you dont need to define iter() and next() method
2) you dont need to define StopIteration exception
"""