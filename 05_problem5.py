# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, sum):
        result = vector(self.x + sum.x, self.y+sum.y, self.z+sum.z)
        return result

    def __mul__(self, prod):
        result = self.x * prod.x + self.y * prod.y + self.z * prod.z
        return result

    def __str__(self):
        return f"Vector {self.x}, {self.y}, {self.z}"

# test implementation
v1 = vector(1,3,5)
v2 = vector(7,9,11)
v3= vector(13,15,17) # same dimension vectors
print(v1+v2)
print(v1 * v2)

print(v1+v3)
print(v1*v3)

v_sum = v1 + v2 + v3
print(v_sum)

v_prod = v1 * v3
print(v_prod)