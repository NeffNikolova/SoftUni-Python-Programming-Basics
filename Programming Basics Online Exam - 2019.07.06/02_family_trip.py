budget = float(input())
nights = int(input())
price_night = float(input())
additional_expense_percent = int(input()) / 100

if nights > 7:
    price_night *= 0.95
else:
    price_night *= 1

total_cost = (price_night * nights) + (budget * additional_expense_percent)
difference = abs(total_cost - budget)

if budget >= total_cost:
    print(f'Ivanovi will be left with {difference:.2f} leva after vacation.')
else:
    print(f'{difference:.2f} leva needed.')
