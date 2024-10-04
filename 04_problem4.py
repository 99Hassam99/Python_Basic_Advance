# Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f'the square is: {self.n*self.n}')

    def cube(self):
        print(f'the cube is: {self.n*self.n*self.n}')

    def square_root(self):
        print(f'the square_root is: {self.n**1/2}')

    @staticmethod
    def hello():
        print("Hello")

a=calculator(4)
a.square()
a.cube()
a.square_root()
a.hello()