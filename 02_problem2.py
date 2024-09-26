# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# example of input data by user
letter = '''
Dear </Name/>,
You are selected!
</Date/>
'''
name =input("Enter your name: ")
date =input("Enter the date: ")

filled_letter = letter.replace("</Name/>",name).replace("</Date/>",date)

print(filled_letter)

# example without user input

letter=''' 
Dear </Name/>,
You are selected!
</Date/>
'''

print(letter.replace("</Name/>","Hassam").replace("</Date/>","26-09-2024")) # .replace chaining