daily_target = int(input())
service = input()

success = False
income = 0

while service != 'closed':
    if service == 'haircut':
        detail = input()
        if detail == 'mens':
            income += 15
        elif detail == 'ladies':
            income += 20
        elif detail == 'kids':
            income += 10
    elif service == 'color':
        detail = input()
        if detail == 'touch up':
            income += 20
        elif detail == 'full color':
            income += 30

    if income < daily_target:
        service = input()
    else:
        success = True
        break

if success:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {(daily_target - income)}lv. more.")

print(f"Earned money: {income}lv.")
