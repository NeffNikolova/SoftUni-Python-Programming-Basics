money = float(input())
year = int(input())

age = 17
expenses = 0

for year in range(1800, year + 1):
    age += 1
    if year % 2 == 0:
        expenses = 12000
    else:
        expenses = (12000 + (age * 50))

    money -= expenses

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')
