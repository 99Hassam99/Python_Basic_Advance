# Can we have a set with 18 (int) and '18' (str) as a value in it?

s={18,"18"}
print(s)
print(type(s))

# or

a=set()
a.add(18)
a.add("18")