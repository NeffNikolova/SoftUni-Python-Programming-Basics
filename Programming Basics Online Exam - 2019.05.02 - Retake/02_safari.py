budget = float(input())
fuel_needed_l = float(input())
weekday = input()

fuel_price_l = 2.10
tour_guide_price = 100

final_expense = 0
diff = 0
total_expense = fuel_needed_l * fuel_price_l + tour_guide_price


if weekday == 'Saturday':
    final_expense = total_expense * 0.90
    diff = abs(budget - final_expense)
    if final_expense >= budget:
        print(f'Not enough money! Money needed: {diff:.2f} lv.')
    else:
        print(f'Safari time! Money left: {diff:.2f} lv. ')
else:
    final_expense = total_expense * 0.80
    diff = abs(budget - final_expense)
    if final_expense >= budget:
        print(f'Not enough money! Money needed: {diff:.2f} lv.')
    else:
        print(f'Safari time! Money left: {diff:.2f} lv. ')