from math import floor, ceil

wine_yard_m2 = int(input())
grapes_per_m2_kg = float(input())
needed_wine_to_sell_l = int(input())
workers_nr = int(input())

total_grapes_kg = wine_yard_m2 * grapes_per_m2_kg
total_wine_l = total_grapes_kg * 0.40/ 2.5

difference = 0
excess_per_worker = 0

if total_wine_l < needed_wine_to_sell_l:
    difference = floor(needed_wine_to_sell_l - total_wine_l)
    print(f'It will be a tough winter! More {difference} liters wine needed.')
else:
    total_wine_l = floor(total_grapes_kg * 0.40 / 2.5)
    difference = ceil(total_wine_l - needed_wine_to_sell_l)
    excess_per_worker = ceil(difference / workers_nr)
    print(f'Good harvest this year! Total wine: {total_wine_l} liters.')
    print(f'{difference} liters left -> {excess_per_worker} liters per person.')



