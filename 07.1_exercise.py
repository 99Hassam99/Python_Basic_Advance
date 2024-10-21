# Codebasics code

# 1. Write a function called calculate_area that takes base
# and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape


def calcolate_area(dimension1,dimension2,shape='triangle'):
    '''
       :param dimension1: In case of triangle it is "base". For rectangle it is "length".
       :param dimension2: In case of triangle it is "height". For rectangle it is "width".
       :param shape: Either "triangle" or "rectangle"
       :return: Area of a shape
       '''
    if shape == 'triangle':
        area = (1 / 2)*(dimension1*dimension2)
    elif shape == 'rectangle':
        area = dimension1*dimension2
    else:
        print('Error: Input shape is neither triangle nor rectangle')
        area=None
    return area

# Calculate area of triangle whose base is 10 and height is 5
base=10
height=5
triangle_area=calcolate_area(base,height,'triangle')
print('area of triangle is:', triangle_area)

# Calculate area of a rectangle whose length is 20 and width is 30
length = 20
width = 30
rect_area = calcolate_area(length,width,'rectangle')
print('area of rectangle is:', rect_area)


# Calculate area of a triangle without supplying shape argument in a function call
triangle_area2=calcolate_area(base,height)
print('area of triangle withut shape:',triangle_area2)








#
# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

'''
:param n: Integer number representing number of lines
     to be printed in a pattern. If n=3 it will print,
    *
     **
    ***
  If n=4, it will print,
    *
    **
    ***
       ****
     Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
'''

def print_pattern(n=5):

    for i in range(n):
        s=''
        for j in range(i):
            s+='*'
        print(s)
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines

# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
print('print pattern with input=3')
print_pattern(3)

print('print pattern with input=4')
print_pattern(4)

print("Print pattern with no input number")
print_pattern() # Not supplying any input will use default argument which is 5