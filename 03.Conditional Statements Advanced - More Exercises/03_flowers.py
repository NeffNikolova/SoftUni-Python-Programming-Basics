chrysanthemum_nr = int(input())
rose_nr = int(input())
tulip_nr = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
price_all = 0

if season.lower() == 'spring' or season.lower() == 'summer':
    chrysanthemum_price = 2
    rose_price = 4.10
    tulip_price = 2.50
    if holiday.lower() == 'y':
        chrysanthemum_price *= 1.15
        rose_price *= 1.15
        tulip_price *= 1.15
        price_all = chrysanthemum_price * chrysanthemum_nr + rose_price * rose_nr + tulip_price * tulip_nr
        if season.lower() == 'spring' and tulip_nr > 7:
            price_all *= 0.95
    if holiday.lower() == 'n':
        price_all = chrysanthemum_price * chrysanthemum_nr + rose_price * rose_nr + tulip_price * tulip_nr
        if season.lower() == 'spring' and tulip_nr > 7:
            price_all *= 0.95
elif season.lower() == 'autumn' or season.lower() == 'winter':
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
    price_all = chrysanthemum_price * chrysanthemum_nr + rose_price * rose_nr + tulip_price * tulip_nr
    if holiday.lower() == 'y':
        chrysanthemum_price *= 1.15
        rose_price *= 1.15
        tulip_price *= 1.15
        price_all = chrysanthemum_price * chrysanthemum_nr + rose_price * rose_nr + tulip_price * tulip_nr
        if season.lower() == 'winter' and rose_nr >= 10:
            price_all *= 0.90
    elif holiday.lower() == 'n':
        price_all = chrysanthemum_price * chrysanthemum_nr + rose_price * rose_nr + tulip_price * tulip_nr
        if season.lower() == 'winter' and rose_nr >= 10:
            price_all *= 0.90

if chrysanthemum_nr + rose_nr + tulip_nr > 20:
    price_all *= 0.80
    price_all += 2
else:
    price_all += 2

print(f'{price_all:.2f}')
