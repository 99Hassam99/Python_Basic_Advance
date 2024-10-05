# Write __str__() method to print the vector as follows:
#  7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        result = vector(self.i+other.i , self.j+other.j, self.k+other.k)
        return result

    def __mul__(self, other):
        result = self.i * other.i + self.j * other.j + self.k * other.k
        return result

    def __str__(self):
        return f'Vector: {self.i}i + {self.k}k + {self.j}j'

v1 = vector(1,2,3)
v2 = vector(4,5,6)

print(v1+v2)
print(v1*v2)