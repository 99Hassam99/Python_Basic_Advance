# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.
class complex:
    def __init__(self,r,i):
        self.i = i
        self.r= r

    def __add__(self, c2):
        return complex(self.r+c2.r , self.i+c2.i)

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = complex(1,2)
c2 = complex(3,4)
print(c1 + c2)
print(c1 * c2)



"""

### Complex Numbers:
A complex number is of the form:
z = a + bi
Where:
- a is the real part
- b is the imaginary part
- i is the imaginary unit, where i^2 = -1 

1. Addition of Complex Numbers:
If we have two complex numbers:
z_1 = a_1 + b_1i
z_2 = a_2 + b_2i
Their sum is given by:
z_1 + z_2 = (a_1 + a_2) + (b_1 + b_2)i
You just add the real parts together and the imaginary parts together.

2. Multiplication of Complex Numbers:
If we have two complex numbers:
z_1 = a_1 + b_1i  &  z_2 = a_2 + b_2i

Their product is given by the distributive property:
z_1.z_2 = (a_1 + b_1i).(a_2 + b_2i)

Expanding this:
z_1.z_2 = a_1a_2 + a_1b_2i + b_1a_2i + b_1b_2i^2 
Since i^2 = -1 , the expression simplifies to:
z_1.z_2 = a_1a_2 + (a_1b_2 + b_1a_2)i - b_1b_2
This gives:
z_1.z_2 = (a_1a_2 - b_1b_2) + (a_1b_2 + b_1a_2)i
Thus, the real part is a_1a_2 - b_1b_2, and the imaginary part is a_1b_2 + b_1a_2.

c1 = 1 + 2i and c2 = 3 + 4i:
1.Addition:
   - Real part: 1 + 3 = 4
   - Imaginary part: 2 + 4 = 6
   So, c1 + c2 = 4 + 6i

2.Multiplication:
   - Real part: 1.3 - 2.4 = 3 - 8 = -5
   - Imaginary part: 1.4 + 2.3 = 4 + 6 = 10
   So,c1.c2 = -5 + 10i


Explanation:
- Addition: (1 + 2i) + (3 + 4i) = 4 + 6i 
- Multiplication: (1 + 2i).(3 + 4i) = -5 + 10i 

"""
