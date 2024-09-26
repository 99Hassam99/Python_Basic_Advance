"""
file open modes r,w,r+,w+,a
with statment
"""
with open("D:\\New folder\\funny.txt","r") as f:
    print(f.read())

print(f.closed) #this f.closed flag will tells if the file is closed or still open
# we dont need to do f.close() if you we use with statement. Using with will automatically close file for you