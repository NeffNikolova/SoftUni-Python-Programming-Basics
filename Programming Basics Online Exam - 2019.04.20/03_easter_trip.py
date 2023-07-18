country = input()
dates = input()
nights = int(input())

night_price = 0

if country == 'France':
    if dates == '21-23':
        night_price = 30
    elif dates == '24-27':
        night_price = 35
    elif dates == '28-31':
        night_price = 40
elif country == 'Italy':
    if dates == '21-23':
        night_price = 28
    elif dates == '24-27':
        night_price = 32
    elif dates == '28-31':
        night_price = 39
elif country == 'Germany':
    if dates == '21-23':
        night_price = 32
    elif dates == '24-27':
        night_price = 37
    elif dates == '28-31':
        night_price = 43

expenses = night_price * nights

print(f'Easter trip to {country} : {expenses:.2f} leva.')