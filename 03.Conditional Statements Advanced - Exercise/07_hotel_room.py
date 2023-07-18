month = input()
nights = int(input())
month = month.lower()

apt_price = 0
studio_price = 0

if month == 'may' or month == 'october':
    if nights > 14:
        studio_price = 50 * 0.70
        apt_price = 65 * 0.90
    elif nights > 7:
        studio_price = 50 * 0.95
        apt_price = 65
    else:
        studio_price = 50
        apt_price = 65
elif month == 'june' or month == 'september':
    if nights > 14:
        studio_price = 75.20 * 0.80
        apt_price = 68.70 * 0.90
    else:
        studio_price = 75.20
        apt_price = 68.70
elif month == 'july' or month == 'august':
    if nights > 14:
        studio_price = 76
        apt_price = 77 * 0.90
    else:
        studio_price = 76
        apt_price = 77

expense_studio = nights * studio_price
expense_apt = nights * apt_price

print(f'Apartment: {expense_apt:.2f} lv.')
print(f'Studio: {expense_studio:.2f} lv.')