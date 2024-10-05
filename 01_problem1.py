# Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class two_D_vector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f'the vector is {self.i}i + {self.j}j')


class three_D_vector(two_D_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f'the vector is {self.i}i + {self.j}j + {self.k}k')

a = two_D_vector(1,2)
a.show()

b = three_D_vector(1,2,3)
b.show()