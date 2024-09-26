"""
In today life we use many devices and tools invented or created by other peoples
for example computer, car or calculator
"""

import math

math.sqrt(16)
print(math.sqrt(16))

math.pow(2,4)
print(math.pow(2,4))

dir(math)
print(dir(math))

math.pi
print(math.pi)

print(math.log10(100))
print(math.log10(1000))

print(math.floor(2.3))
print(math.ceil(2.3))


import calendar
cal=calendar.month(2018,2)
print(cal)

print(calendar.isleap(2018))
print(calendar.isleap(2024))

print(dir(calendar))

#import with the name of moduel file
#import module.module2Functions as f #used for import function outside the directory
#sys.path.append("C:\code")

import module2Functions as f
area=f.calculate_square_area(5)
print(area)

triangle=f.calculate_triangle_area(5,10)
print(triangle)