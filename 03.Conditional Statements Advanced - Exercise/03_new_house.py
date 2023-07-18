flower_type = input()
quantity = int(input())
budget = int(input())

expense = 0

if flower_type == 'Roses':
    if quantity > 80:
        expense = quantity * 5 * 0.90
    else:
        expense = quantity * 5
elif flower_type == 'Dahlias':
    if quantity > 90:
        expense = quantity * 3.80 * 0.85
    else:
        expense = quantity * 3.80
elif flower_type == 'Tulips':
    if quantity > 80:
        expense = quantity * 2.80 * 0.85
    else:
        expense = quantity * 2.80
elif flower_type == 'Narcissus':
    if quantity < 120:
        expense = quantity * 3 * 1.15
    else:
        expense = quantity * 3
elif flower_type == 'Gladiolus':
    if quantity < 80:
        expense = quantity * 2.50 * 1.20
    else:
        expense = quantity * 2.50

diff = abs(expense-budget)
if expense <= budget:
    print(f"Hey, you have a great garden with {quantity} {flower_type} and {diff:.2f} leva left.")
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')

