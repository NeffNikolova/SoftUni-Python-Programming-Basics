budget = float(input())
destination = input()
season = input()
days = int(input())

expenses = 0
factor = 1

if destination.lower() == 'dubai':
    factor = 0.70
    if season.lower() == 'winter':
        expenses = (days * 45000) * factor
    elif season.lower() == 'summer':
        expenses = (days * 40000) * factor
if destination.lower() == 'sofia':
    factor = 1.25
    if season.lower() == 'winter':
        expenses = (days * 17000) * factor
    elif season.lower() == 'summer':
        expenses = (days * 12500) * factor
if destination.lower() == 'london':
    if season.lower() == 'winter':
        expenses = (days * 24000) * factor
    elif season.lower() == 'summer':
        expenses = (days * 20250) * factor

diff = abs(budget - expenses)

if budget >= expenses:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')