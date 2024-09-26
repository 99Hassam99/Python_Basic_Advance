Peshawari=("Karahi","Tikka","Mutton","rice")
Karachi=("Biryani","Chicken karahi")
Fastfood=("Burger","Pasta","Pizza")

dish=input("Enter a dish name: ")

if dish in Peshawari:
    print("Peshawari")
elif dish in Karachi:
    print("Karachi")
elif dish in Fastfood:
    print("Fast Food")
else:
    print("Unknown",dish)