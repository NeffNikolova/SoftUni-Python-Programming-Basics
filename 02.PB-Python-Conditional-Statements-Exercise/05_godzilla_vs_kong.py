movie_budget = float(input())
nr_statists = int(input())
price_clothing_statist = float(input())

price_decor = movie_budget * 0.1

final_price_clothing_statist = 0
difference = 0

if nr_statists > 150:
    final_price_clothing_statist = 0.90 * price_clothing_statist
else:
     final_price_clothing_statist = price_clothing_statist

final_expences = (final_price_clothing_statist * nr_statists) + price_decor

if final_expences > movie_budget:
    difference = final_expences - movie_budget
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    difference = movie_budget - final_expences
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')