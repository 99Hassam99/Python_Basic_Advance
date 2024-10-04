"""
an object is an instance

 Instance attributes, take preference over class attributes during assignment &
retrieval.

When looking up for hassam.attribute it checks for the following:
1) Is attribute present in object?
2) Is attribute present in class?
"""

class Employee:
    language ="Python"
    salary=120000

hassam = Employee()
hassam.language="Dart"
print(hassam.language,hassam.salary)