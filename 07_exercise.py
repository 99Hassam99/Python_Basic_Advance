# hassam code

# Functions
# 1. Write a function called calculate_area that takes base
# and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def cal_area():
    base = int(input('Enter a number: '))
    height = int(input('Enter a number: '))

    area = (1/2)*base*height
    print(area)

cal_area()


# 2. Modify above function to take third parameter shape type.
# It can be either "triangle" or "rectangle". Based on shape type
# it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calucalte_area():
    length = int(input('Enter a number: '))
    width = int(input('Enter a number: '))
    rectangle_area=length*width
    print(rectangle_area)

calucalte_area()


# 3. Write a function called print_pattern that takes
# integer number as an argument and prints following pattern if input number is 3,
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

def print_pattern(n=5):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s+="*"
        print(s)

print_pattern()



