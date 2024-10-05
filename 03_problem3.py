# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=4

o=Demo()
print(o.a) # prints the class attribute because instance attribute is not present
o.a=0 # object attribute is changed to 0 | instance attribute is set
print(o.a) # prints the instance attribute because instance attribute is present
print(Demo.a) # prints the class attribute | so the answer of this question is (NO) because the class attribute is still 4 which is not changed