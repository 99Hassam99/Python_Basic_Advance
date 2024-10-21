# Using following list of cities per country,

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# Write a program that asks user to enter a city name, and it should tell which country the city belongs to
# Write a program that asks user to enter two cities, and it tells
# you if they both are in same country or not. For example if I enter mumbai and
# chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka
# it should print "They don't belong to same country"


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = str(input("Enter city name: "))

if city in india:
    print("city belongs to India")
elif (city in pakistan):
    print("city belongs to Pakistan")
elif (city in bangladesh):
    print("city belongs to Bangladesh")
else:
    print(f'i wont be able tell you which country {city} is in! sorry')

