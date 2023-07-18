budget = float(input())
category = input()
number_people = int(input())

ticket_price = 0
all_tickets_price = 0

if category == 'VIP':
    ticket_price = 499.99
    if number_people <= 4:
        budget *= 0.25
    elif number_people <= 9:
        budget *= 0.40
    elif number_people <= 24:
        budget *= 0.50
    elif number_people <= 49:
        budget *= 0.60
    elif number_people >= 50:
        budget *= 0.75
elif category == 'Normal':
    ticket_price = 249.99
    if number_people <= 4:
        budget *= 0.25
    elif number_people <= 9:
        budget *= 0.40
    elif number_people <= 24:
        budget *= 0.50
    elif number_people <= 49:
        budget *= 0.60
    elif number_people >= 50:
        budget *= 0.75

all_tickets_price = number_people * ticket_price

diff = abs(all_tickets_price - budget)

if all_tickets_price <= budget:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

