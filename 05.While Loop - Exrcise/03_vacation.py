funds_needed = float(input())
budget = float(input())

spend_in_row = 0
days = 0

while True:
    action = input()
    amount = float(input())
    days += 1
    if action == 'spend':
        spend_in_row += 1
        if spend_in_row == 5:
            print("You can't save the money.")
            print(f'{days}')
            break
        elif budget - amount <= 0:
            budget = 0
        else:
            budget -= amount
    elif action == 'save':
        budget += amount
        spend_in_row = 0
        if budget >= funds_needed:
            print(f'You saved the money for {days} days.')
            break
        else:
            continue
