import math

excursion_cost = float(input())
nr_puzzle = int(input())
nr_doll = int(input())
nr_teddy = int(input())
nr_minion = int(input())
nr_truck = int(input())

price_puzzle = 2.60
price_doll = 3
price_teddy = 4.10
price_minion = 8.20
price_truck = 2

all_order_nr = nr_puzzle + nr_doll + nr_teddy + nr_minion + nr_truck

income = (nr_doll * price_doll) +(nr_truck * price_truck) + (nr_puzzle * price_puzzle) + (nr_minion * price_minion) + \
         + (nr_teddy * price_teddy)

if all_order_nr >= 50:
    income = (income * 0.75) * 0.9
else:
    income = income * 0.9

if income >= excursion_cost:
    rest = income - excursion_cost
    print(f'Yes! {rest:.2f} lv left.')
else:
    rest = excursion_cost - income
    print(f'Not enough money! {rest:.2f} lv needed.')

