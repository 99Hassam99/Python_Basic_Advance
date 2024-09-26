"""
Set is an unordered collection of unique elements
in sets we cannot access index as it is unordered which is allowed by list.
List allows index operation, set doesn't allow it.
List allows duplicate elements, set doesn't allow it.

"""

basket = {"orange", "grapes", "Mangoes", "apple", "orange", "apple"}
print(type(basket))
print(basket)
a = set(basket)
a.add("ABC")
print(a)
a = {"SA"}
print(type(a))
a = {}  # empty curly brackets will always recall dictionary
print(type(a))

numbers = [1, 2, 3, 4, 4, 3, 2, 1]
unique_number = set(numbers)
unique_number.add(5)
print(unique_number)
fs = frozenset(numbers)
print(fs)  # frozenset does not allow to add new element while simple set allows it

x = {'a', 'b', 'c'}
print("a" in x)
print("g" in x)
for i in x:
    print(i)

y = {'a', 'g', 'h'}
print(y)
print(x)
print(x | y)  # for union
print(x & y)  # for intersection
print(x - y)  # for difference
z = {'g', 'h'}
print(z < y)  # for subset
