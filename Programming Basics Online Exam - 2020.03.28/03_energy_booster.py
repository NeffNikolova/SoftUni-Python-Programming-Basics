fruit = input()
size = input()
sets_nr = int(input())

packs_in_set = 0
pack_price = 0
discount = 0

if size == 'small':
    packs_in_set = 2
    if fruit == 'Watermelon':
        pack_price = 56
    elif fruit == 'Mango':
        pack_price = 36.66
    elif fruit == 'Pineapple':
        pack_price = 42.10
    elif fruit == 'Raspberry':
        pack_price = 20
if size == 'big':
    packs_in_set = 5
    if fruit == 'Watermelon':
        pack_price = 28.70
    elif fruit == 'Mango':
        pack_price = 19.60
    elif fruit == 'Pineapple':
        pack_price = 24.80
    elif fruit == 'Raspberry':
        pack_price = 15.20

expenses = sets_nr * packs_in_set * pack_price

if 400 <= expenses <= 1000:
    expenses *= 0.85
elif expenses > 1000:
    expenses *= 0.50

print(f'{expenses:.2f} lv.')
