budget = float(input())
season = input()

destination = None
facility = None
expense = 0

if budget > 1000:
    destination = 'Europe'
    facility = 'Hotel'
    expense = budget * 0.90
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expense = budget * 0.40
        facility = 'Camp'
    elif season == 'winter':
        expense = budget * 0.80
        facility = 'Hotel'
elif budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expense = budget * 0.30
        facility = 'Camp'
    elif season == 'winter':
        expense = budget * 0.70
        facility = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{facility} - {expense:.2f}')