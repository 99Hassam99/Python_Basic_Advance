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

city1 = str(input("Enter city name: "))
city2 = str(input("Enter city name: "))

if city1 in india and city2 in india:
    print("Both cities belongs to India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities belongs to Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities belongs to Bangladesh")
else:
    print('They dont belong to same country! Sorry!')
