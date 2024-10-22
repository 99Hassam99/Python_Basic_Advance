# 1. Create an iterator for fibonacci series in such a way that each next returns
# the next element from fibonacci series.

# 2. The iterator should stop when it reaches a limit defined in the constructor.

class fibnocci:
    def __init__(self,limit):
        # default constructor
        self.previous=0
        self.current=1
        self.n=1
        self.limit = limit
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result= self.previous + self.current
            self.previous = self.current
            self.current =result
            self.n += 1
            return result
        else:
            raise StopIteration

# init the fib_iterator
fib_iter = iter(fibnocci(5))
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iter))
    except StopIteration:
        break