joinery_nr = int(input())
joinery_type = input()
delivery = input()

expenses = 0
price = 0
delivery_price = 0

if joinery_type.lower() == '90x130':
    price = 110
    if 30 < joinery_nr <= 60:
        price *= 0.95
    if joinery_nr > 60:
        price *= 0.92
elif joinery_type.lower() == '100x150':
    price = 140
    if 40 < joinery_nr <= 80:
        price *= 0.94
    if joinery_nr > 80:
        price *= 0.90
elif joinery_type.lower() == '130x180':
    price = 190
    if 20 < joinery_nr <= 50:
        price *= 0.93
    if joinery_nr > 50:
        price *= 0.88
elif joinery_type.lower() == '200x300':
    price = 250
    if 25 < joinery_nr <= 50:
        price *= 0.91
    if joinery_nr > 50:
        price *= 0.86

if delivery.lower() == 'with delivery':
    delivery_price += 60

if joinery_nr < 10:
    print(f'Invalid order')
elif joinery_nr > 99:
    expenses = ((price * joinery_nr) + delivery_price) * 0.96
    print(f'{expenses:.2f} BGN')
else:
    expenses = ((price * joinery_nr) + delivery_price)
    print(f'{expenses:.2f} BGN')


