# Write a class “Calculator” capable of finding square, cube and square root of a
# number

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f'the square is: {self.n*self.n}')

    def cube(self):
        print(f'the cube is: {self.n*self.n*self.n}')

    def square_root(self):
        print(f'the square_root is: {self.n**1/2}')


a=calculator(4)
a.square()
a.cube()
a.square_root()