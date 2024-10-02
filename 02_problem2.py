# 2. Write a python program using function to convert Celsius to Fahrenheit.

def temperature(f):
        c = 5*(f-32)/9
        return c
f=int(input("Enter Temp in fehrenhiet: "))
print(f"Temperature in celsius is:{round(temperature(f),2)}°C:")




def temperature(c):
     f = 9/5*c+32
     return f

celsius=float(input("Enter Temp in celsius: "))
fehrenheit=temperature(celsius)
print(f'The temp in fehrenheit is:{round(fehrenheit,2)}°F')