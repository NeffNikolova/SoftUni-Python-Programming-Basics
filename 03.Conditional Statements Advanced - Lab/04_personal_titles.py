age = float(input())
gender = input()
title = None

if gender == 'm':
    if age < 16:
        title = 'Master'
    elif age >= 16:
        title = 'Mr.'
else:
    if age < 16:
        title = 'Miss'
    elif age >= 16:
        title = 'Ms.'

print(title)