"""
we want to create new file that has all the lines
in funnt.txt plus word count for each line
"""
f=open("D:\\New folder\\funny.txt","r")
f_out=open("D:\\New folder\\funny_wc.txt","w")

for line in f:
    tokens=line.split(" ") #split will split the string using input character and return a list(array) of words
    f_out.write("word count: "+str(len(tokens))+line)
 #   print(len(tokens))

f.close()
f_out.close()

"""
print(f.read())
f.close()
"""