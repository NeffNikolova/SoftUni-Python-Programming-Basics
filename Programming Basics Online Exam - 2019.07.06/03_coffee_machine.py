drink = input()
sugar = input()
drinks_nr = int(input())

expenses = 0
discount = 0
price = 0

if drink.lower() == 'espresso':
    if sugar.lower() == 'without':
        expenses = 0.90 * drinks_nr * (1 - 0.35)
        if drinks_nr >= 5:
            expenses *= 0.75
    elif sugar.lower() == 'normal':
        expenses = 1 * drinks_nr
        if drinks_nr >= 5:
            expenses *= 0.75
    elif sugar.lower() == 'extra':
        expenses = 1.20 * drinks_nr
        if drinks_nr >= 5:
            expenses *= 0.75
elif drink.lower() == 'cappuccino':
    if sugar.lower() == 'without':
        expenses = 1 * drinks_nr * (1 - 0.35)
    elif sugar.lower() == 'normal':
        expenses = 1.20 * drinks_nr
    elif sugar.lower() == 'extra':
        expenses = 1.60 * drinks_nr
elif drink.lower() == 'tea':
    if sugar.lower() == 'without':
        expenses = 0.50 * drinks_nr * (1 - 0.35)
    elif sugar.lower() == 'normal':
        expenses = 0.60 * drinks_nr
    elif sugar.lower() == 'extra':
        expenses = 0.70 * drinks_nr

if expenses > 15:
    expenses *= 0.80

print(f'You bought {drinks_nr} cups of {drink} for {expenses:.2f} lv.')


