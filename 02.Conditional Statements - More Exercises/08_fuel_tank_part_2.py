fuel = input() #Gas, Gasoline, Diesel
fuel_needed = float(input())
club_card = input() #yes, no

fuel_price = 0

# if fuel == 'Gas':
#     if club_card == 'Yes':
#         fuel_price = 0.93 - 0.08
#     else:
#         fuel_price = 0.93
# elif fuel == 'Gasoline':
#     if club_card == 'Yes':
#         fuel_price = 2.22 - 0.18
#     else:
#         fuel_price = 2.22
# elif fuel == 'Diesel':
#     if club_card == 'Yes':
#         fuel_price = 2.33 - 0.12
#     else:
#         fuel_price = 2.33
#
# total_price = fuel_price * fuel_needed
#
# if fuel_needed > 25:
#     total_price *= 0.90
# elif fuel_needed > 20:
#     total_price *= 0.92
# else:
#     total_price *= 1

if fuel == 'Gas' and club_card == 'Yes':
    fuel_price = 0.93 - 0.08
elif fuel == 'Gas' and club_card == 'No':
    fuel_price = 0.93
elif fuel == 'Gasoline' and club_card == 'Yes':
    fuel_price = 2.22 - 0.18
elif fuel == 'Gasoline' and club_card == 'No':
    fuel_price = 2.22
elif fuel == 'Diesel' and club_card == 'Yes':
    fuel_price = 2.33 - 0.12
elif fuel == 'Diesel' and club_card == 'No':
    fuel_price = 2.33

total_price = fuel_price * fuel_needed

if fuel_needed > 25:
    total_price *= 0.90
elif fuel_needed > 20:
    total_price *= 0.92

print(f'{total_price:.2f} lv.')

