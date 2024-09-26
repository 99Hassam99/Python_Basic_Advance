import os

# specify the directory you want to list
directory_path = '/'

# List all the files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory
for item in contents:
    print(item)
