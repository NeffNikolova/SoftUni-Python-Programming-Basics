budget = int(input())
season = input()
fishermen_nr = int(input())

expense = 0

if season == 'Spring':
    if fishermen_nr <= 6:
        expense = 3000 * 0.90
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95
    elif 7 <= fishermen_nr <= 11:
        expense = 3000 * 0.85
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95
    elif 12 < fishermen_nr:
        expense = 3000 * 0.75
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95
elif season == 'Summer' or season == 'Autumn':
    if fishermen_nr <= 6:
        expense = 4200 * 0.90
        if fishermen_nr % 2 == 0 and season != 'Autumn':
            expense = expense * 0.95
    elif 7 <= fishermen_nr <= 11:
        expense = 4200 * 0.85
        if fishermen_nr % 2 == 0 and season != 'Autumn':
            expense = expense * 0.95
    elif 12 < fishermen_nr:
        expense = 4200 * 0.75
        if fishermen_nr % 2 == 0 and season != 'Autumn':
            expense = expense * 0.95
if season == 'Winter':
    if fishermen_nr <= 6:
        expense = 2600 * 0.90
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95
    elif 7 <= fishermen_nr <= 11:
        expense = 2600 * 0.85
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95
    elif 12 < fishermen_nr:
        expense = 2600 * 0.75
        if fishermen_nr % 2 == 0:
            expense = expense * 0.95

diff = abs(expense - budget)

if budget >= expense:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')