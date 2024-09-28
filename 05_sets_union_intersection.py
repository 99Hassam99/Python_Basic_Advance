# Returns a new set with all items from both sets. {1,8,2,3,11}.
s1={1,2,3,4}
s2={3,4,5,6,7,8}

print(s1.union(s2)) # it joins both s1 and s2

print(s1.intersection(s2)) # it took only same values from s1 and s2

print({1,2}.issubset(s1))

print(s1.issuperset({1,9}))