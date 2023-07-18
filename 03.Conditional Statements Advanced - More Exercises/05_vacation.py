budget = float(input())
season = input()

cost = 0
accommodation = ''
location = ''

if budget <= 1000:
    accommodation = 'Camp'
    if season.lower() == 'summer':
        location = 'Alaska'
        cost = budget * 0.65
    elif season.lower() == 'winter':
        location = 'Morocco'
        cost = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season.lower() == 'summer':
        location = 'Alaska'
        cost = budget * 0.8
    elif season.lower() == 'winter':
        location = 'Morocco'
        cost = budget * 0.60
elif budget > 3000:
    accommodation = 'Hotel'
    cost = budget * 0.9
    if season.lower() == 'summer':
        location = 'Alaska'
    elif season.lower() == 'winter':
        location = 'Morocco'

print(f'{location} - {accommodation} - {cost:.2f}')





