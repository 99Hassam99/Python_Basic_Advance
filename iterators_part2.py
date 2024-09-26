"""
Implement a remote control class that allows you to press next button
to go next TV channel
"""
class RemoteConrtol():
    def __init__(self):
        self.channels=['HBO',"GEO","Tensports",'espn']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r=RemoteConrtol()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))