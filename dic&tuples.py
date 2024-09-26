"""
dictionaries allow to store key value pairs
also knows as MAPS , HASHTABLES,Associate arrays
//classical example is telephone directory
"""

d={"tom":73123211, "rob":21432112,"joe":23184291}

print("directory:",d)

print("Tom number",d["tom"])

d["Shaq"]=3130422253
print(d)

del d["tom"]
print(d)

for key in d:
    print("key:",key,"value:",d[key])

#tuples
# tuples is nothing but a list of values grouped together
for k,v in d.items():
    print("key:",key,"value:",v)

"sameer" in d

print(d)
"shaq" in d
print(d)

d.clear()
print(d)

"""
tuples vs list
in list all the values have similar meaning (homogenous)
while in tuples all the values have different meaning (heterogenous)
"""

point=(5,9)  #(x coordinate, y coordinate)
point[0]
point[1]

"""
list examples: 
expense_list=[2300,2500,2900,6670] #where every item is an expense

list_of_names=["Bob",'tom','shaq'] #where every item is a name of a person

tuples examples
point=(4,5) #4 is x coordinate, 5 is y coordinate

address=("1 purple street","new york",10001)
"""