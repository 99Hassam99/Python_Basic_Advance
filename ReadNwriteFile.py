'''
in this topic we will learn
1) create new file and write to it
2) reading file line by line
3) file open modes
4) with statement
'''

f=open("D:\\New folder\\funny.txt","a")  #1st side of this parameter is file name and path and 2nd is file open mode
f.write("\n I love you")
f.close()

#this function will be saved until you changed it and run it, all the previous data will be lost, so for saving previous data A PAN is used which is in the starting paratemeter, use a instead of w
