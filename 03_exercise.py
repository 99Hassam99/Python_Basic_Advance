# Exercise: String in Python

# 1. Create 3 variables to store street, city and country,
# now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and
# the other using f-string. Now Print the address in such a way that the street,
# city and country prints in a separate line

street='Street 4 Block P '
city=' Peshawar'
country=' Pakistan'

# one way
address= street + '\n' + city + '\n'+  country
print('address using + operator', address)

print(f'{street}, {city}, {country}')
print(f'Street:{street},\n City:{city}.\n Country: {country}')


# 2. Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

quote = "Earth revolves around the sun"

ind= len(quote)
print(ind)

print(quote[6:14])

print(quote[-3:])



# 3. Create two variables to store how many fruits and vegetables
# you eat in a day. Now Print "I eat x veggies and y fruits daily" where
# x and y presents vegetables and fruits that you eat every day.
# Use python f string for this.

x_fruits = 5
y_veg = 3

print(f'I eat {y_veg} veggies and {x_fruits} fruits daily')



# 4. I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s= 'maine 200 banana khaye'
replaced_string = s.replace('200 banana','10 samosa')
print('1st method: ',replaced_string)

rep_str = s.replace('banana','samosa').replace('200','10')
print('2nd method: ', rep_str)