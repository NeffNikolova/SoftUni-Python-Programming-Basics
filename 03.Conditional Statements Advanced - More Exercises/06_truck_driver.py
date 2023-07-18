season = input()
km_month = float(input())

money = 0

if km_month <= 5000:
    if season.lower() == 'spring' or season.lower() == 'autumn':
        money = km_month * 0.75
    elif season.lower() == 'summer':
        money = km_month * 0.90
    elif season.lower() == 'winter':
        money = km_month * 1.05
if 5000 < km_month <= 10000:
    if season.lower() == 'spring' or season.lower() == 'autumn':
        money = km_month * 0.95
    elif season.lower() == 'summer':
        money = km_month * 1.10
    elif season.lower() == 'winter':
        money = km_month * 1.25
if 10000 < km_month:
        money = km_month * 1.45

money *=0.90 * 4

print(f'{money:.2f}')