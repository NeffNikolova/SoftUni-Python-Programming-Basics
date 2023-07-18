from math import ceil

people_nr = int(input())
entry_fee = float(input())
lounger_fee = float(input())
umbrella_fee = float(input())

umbrellas_needed = ceil(people_nr / 2)
# print(umbrellas_needed)
loungers_needed = ceil(0.75 * people_nr)
# print(loungers_needed)
funds_needed = (loungers_needed * lounger_fee) + (people_nr * entry_fee) + (umbrella_fee * umbrellas_needed)

print(f'{funds_needed:.2f} lv.')
