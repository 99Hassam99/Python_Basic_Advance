# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.


word = "donkey"

with open("04_file.txt","r") as f:
    content = f.read()

content_New=content.replace("donkey","####")

with open("04_file.txt","w") as f:
    f.write(content_New)