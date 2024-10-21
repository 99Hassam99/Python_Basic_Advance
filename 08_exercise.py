# Python Dict and Tuples

# 1. We have the following information on countries and their population (population is in crores),
#
# Country	Population
# China	     147
# India	     150
# USA	      38
# Pakistan	  25

# i. Using above create a dictionary of countries and its population
# ii. Write a program that asks user for three type of inputs,
#    a.print: if user enter print then it should print all countries with their population in this format,
#      china==>143
#      india==>136
#      usa==>32
#      pakistan==>21
#    b.add: if user input add then it should further ask for a country name to add.
#       If country already exist in our dataset then it should print that it exist and do nothing.
#       If it doesn't then it asks for population and add that new country/population in our dictionary and print it.
#    c. remove: when user inputs remove it should ask for a country to remove.
#      If country exist in our dictionary then remove it and print new dictionary
#      using format shown above in (a). Else print that country doesn't exist!
#    d. query: on this again ask user for which country he or she wants to query.
#      When user inputs that country it will print population of that country.


countries_population={
    'china':147,
    'india':150,
    'usa':38,
    'pakistan':25
}

def add():
    country=input('Enter country name to add: ')
    country=country.lower()
    if country in countries_population:
        print('Country already exits')
        return
    p=input(f'Enter population for {country}')
    p=float(p)
    countries_population[country]=p
    print_all()

def remove():
    country=input('enter country to remove:')
    country=country.lower()
    if country not in countries_population:
        print('country doesnt exit.')
        return
    del countries_population[country]
    print_all()

def query():
    country = input('enter country name to query: ')
    country=country.lower()
    if country not in countries_population:
        print('country doesnt exist:')
        return
    print(f'population of {country} is: {countries_population[country]} crore')


def print_all():
    for country, p in countries_population.items():
        print(f'{country}==>{p}')

def main():
    op = input('Enter operation(add,remove,query or print:)')
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__=='__main__':
    main()