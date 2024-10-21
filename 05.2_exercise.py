# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar = int(input("Enter Fasting sugar level:"))
sugar=float(sugar)
if sugar < 80:
    print("sugar is low")
elif sugar > 100:
    print('Sugar is high')
else:
    print("normal")