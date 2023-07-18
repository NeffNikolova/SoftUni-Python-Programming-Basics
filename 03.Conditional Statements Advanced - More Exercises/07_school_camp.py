season = input()
group_type = input()
students_nr = int(input())
nights_nr = int(input())

factor_discounted = 1
single_night_price = 0
sport = ''


if season.lower() == 'winter':
    if group_type == 'mixed':
        single_night_price = 10
        sport = 'Ski'
    else:
        single_night_price = 9.60
        if group_type == 'girls':
            sport = 'Gymnastics'
        elif group_type == 'boys':
            sport = 'Judo'
elif season.lower() == 'spring':
    if group_type == 'mixed':
        single_night_price = 9.50
        sport = 'Cycling'
    else:
        single_night_price = 7.20
        if group_type == 'girls':
            sport = 'Athletics'
        elif group_type == 'boys':
            sport = 'Tennis'
elif season.lower() == 'summer':
    if group_type == 'mixed':
        single_night_price = 20
        sport = 'Swimming'
    else:
        single_night_price = 15
        if group_type == 'girls':
            sport = 'Volleyball'
        elif group_type == 'boys':
            sport = 'Football'


if students_nr >= 50:
    factor_discounted = 0.5
elif 20 <= students_nr < 50:
    factor_discounted = 0.85
elif 10 <= students_nr < 20:
    factor_discounted = 0.95

expenses = (nights_nr * single_night_price * students_nr) * factor_discounted

print(f'{sport} {expenses:.2f} lv.')