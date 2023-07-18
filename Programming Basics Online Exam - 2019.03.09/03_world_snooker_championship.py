stage = input()
ticket_type = input()
ticket_nr = int(input())
trophy_pic = input()

expenses = 0

if stage.lower() == 'quarter final':
    if ticket_type.lower() == 'standard':
        expenses = ticket_nr * 55.50
    elif ticket_type.lower() == 'premium':
        expenses = ticket_nr * 105.20
    elif ticket_type.lower() == 'vip':
        expenses = ticket_nr * 118.90
elif stage.lower() == 'semi final':
    if ticket_type.lower() == 'standard':
        expenses = ticket_nr * 75.88
    elif ticket_type.lower() == 'premium':
        expenses = ticket_nr * 125.22
    elif ticket_type.lower() == 'vip':
        expenses = ticket_nr * 300.40
elif stage.lower() == 'final':
    if ticket_type.lower() == 'standard':
        expenses = ticket_nr * 110.10
    elif ticket_type.lower() == 'premium':
        expenses = ticket_nr * 160.66
    elif ticket_type.lower() == 'vip':
        expenses = ticket_nr * 400

if expenses > 4000:
    expenses *= 0.75
elif expenses > 2500:
    expenses *= 0.90
    if trophy_pic.lower() == 'y':
        expenses += ticket_nr * 40
else:
    if trophy_pic.lower() == 'y':
        expenses += ticket_nr * 40

print(f'{expenses:.2f}')

