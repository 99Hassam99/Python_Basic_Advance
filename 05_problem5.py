# Repeat program 4 for a list of such words to be censored.

words = ["donkey","tum",'hosh','nahi']

with open("04_file.txt","r") as f:
    content = f.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open("04_file.txt","w") as f:
    f.write(content)