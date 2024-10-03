# Write a program to mine a log file and find out whether it contains ‘python’

with open("06_log.txt.html",'r')as f:
    content = f.read()

if("python" in content):
    print("Yes python is present in Log file")
else:
    print("Yes python is  not present in Log file")
