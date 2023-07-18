from math import ceil

nr_guests = int(input())
budget = int(input())

challah_bread_price = 4
egg_price = 0.45

challah_bread_nr = ceil(nr_guests / 3)
eggs_nr = nr_guests * 2

cost = challah_bread_nr * challah_bread_price + eggs_nr * egg_price

diff  = abs(budget - cost)

if budget >= cost:
    print(f'Lyubo bought {challah_bread_nr} Easter bread and {eggs_nr} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')
