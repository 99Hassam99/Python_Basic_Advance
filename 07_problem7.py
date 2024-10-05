#  Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

class vector:
    def __init__(self,l):
        self.l = l
        # self.i = i
        # self.j = j
        # self.k = k
    # def __add__(self, other):
    #     result = vector(self.i+other.i, self.j+other.j, self.k+other.k)
    #     return result
    #
    # def __mul__(self, other):
    #     result = self.i * other.i + self.j * other.j + self.k * other.k
    #     return result
    #
    # def __str__(self):
    #     return f"Vector is: {self.i}i + {self.j}j + {self.k}k"
    def __len__(self):
        return len(self.l)

v1=vector([1,2,3])
v2=vector([3,4,5])

# print(v1 + v2)
# print(v1 * v2)
print(len(v1))
print(len(v2))