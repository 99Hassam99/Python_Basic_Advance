"""
list, set and dictionary comprehensions
1) List comprehension  provide a way to transform one list into another
2) set is basically a collection of unique items so the basic difference between
set and list is that set is unordered and it does not allow to contain
duplicate items
3)
"""

# List comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)

# or

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [i for i in numbers if i % 2 == 0]
print(even)

num = [1, 2, 3, 4, 5]
sqr_num = [i * i for i in num]
print(sqr_num)

# set comprehension


s = set([1, 2, 3, 4, 5,2,3]) # we can also use {} curly brackets instead of set([])
print(s)

nim=[1,3,4,6,8,90]
even={ i for i in nim if i%2==0}
print(even)


# dic comprehension

cities = ["Peshawar", "Karachi", "Lahore"]
province = ["KPK", "Sindhi", "Punjab"]
z=zip(cities,province)
print(z)
for a in z:
    print(a)

d = {city:provinc for  city,provinc in zip(cities,province)}
print(d)