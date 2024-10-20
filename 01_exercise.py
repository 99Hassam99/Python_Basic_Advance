# Exercise: Python Variables
# 1.Create a variable called break and assign it a value 5.
# See what happens and find out the reason behind the behavior that you see.

# break=5
# It give an error because a BREAK in python is a loop control statement.
# It is used to control the sequence of the loop.
# it dont take an argument


# 2. Create two variables. One to store your birth year and another
# one to store current year. Now calculate your age using these two variables

birth_year= 2003
current_year=2024

age = current_year - birth_year
print(age)

# 3. Store your first, middle and
# last name in three different variables and then print your full name using these variables

f_name = 'Hassam'
m_name = 'Ahmad'
l_name = 'Qureshi'

full_name = f_name+" "+m_name+" "+l_name
print(full_name)


# 4. Answer which of these are invalid variable names:
# _nation 1record record1 record_one record-one record^one continue

# 1record='' incorrect because python variables always start from a character
record1='' # correct variable
record_one='' # correct variable (snake case)
# record-one='' # incorrect syntax because we cant use single dash.
# record^one='' # we cant use special characters in variables