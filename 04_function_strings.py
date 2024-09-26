name = "Shaq"
print(len(name))
print(name.endswith('aq'))
print(name.endswith('aqa'))
print(name.startswith("Sh")) # it's true
print(name.startswith("sh")) # it's false because of small 's' (python is case-sensitive
print(name.startswith("Ash"))

name2 = 'ahmad is nice kid!'
print(name2.capitalize()) # it will capitalize only the first letter of string capital
print(name2.lower()) # it will make the whole string lower case
print(name2.upper()) # it will make the whole string upper case
print(name2.title()) # it will make the 1st letter of each word capital
print(name2.count('i')) # it counts the total occurrence of any character

str = "Hassam,ahmad,qureshi"
index = str.find("m")
print(index)
replaced_string = str.replace("s",'m')
print(replaced_string)
print(str.split(","))

cars=["fx","mehran","Xli"]
print(",".join(cars))