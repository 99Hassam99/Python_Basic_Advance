# Exercise: Numbers in python
# 1.You have a football field that is 92 meter long
# and 48.8 meter wide. Find out total area using python and print it.
length_field=92.0
witdh_field=48.8
total_area = length_field*witdh_field
print(f'{total_area} square meters')


# 2.You bought 9 packets of potato chips from a store.
# Each packet costs 1.49 dollar, and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?

pck_pot_chips=9
one_pck=1.49
total_paid = pck_pot_chips * one_pck
print('You have paid:',total_paid,"$")
paid_money=20
return_money = paid_money - total_paid
print("Money remain:",return_money,'$')


# 3.You want to replace tiles in your bathroom which is exactly
# square and 5.5 feet is its length. If tiles cost 500 rs per square feet,
# how much will be the total cost to replace all tiles. Calculate and print
# the cost using python (Hint: Use power operator ** to find area of a square)
lengt = 5.5
area=lengt**2 # area of square is length power 2
print(area)
tiles_area_sqr_feet=area
tile_cost_per_sqr_feet= 500

total_cost= tiles_area_sqr_feet*tile_cost_per_sqr_feet
print(total_cost)

# 4.Print binary representation of number 17

num = 18
print(f'binary format of number{num} is: {format(num, 'b')}')
