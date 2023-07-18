from math import ceil
from math import floor

tennis_rackets_price = float(input())
tennis_rackets_nr = int(input())
sneakers_nr = int(input())

sneakers_price = tennis_rackets_price * (1 / 6)

main_equipment_price = (tennis_rackets_price * tennis_rackets_nr) + (sneakers_price * sneakers_nr)
other_equipment_price = 0.2 * main_equipment_price

total_equipment_price = main_equipment_price + other_equipment_price

Price_for_Djokovic = floor(total_equipment_price * (1 / 8))
price_for_sponsors = ceil(total_equipment_price * (7 / 8))

print(f'Price to be paid by Djokovic {Price_for_Djokovic}')
print(f'Price to be paid by sponsors {price_for_sponsors}')