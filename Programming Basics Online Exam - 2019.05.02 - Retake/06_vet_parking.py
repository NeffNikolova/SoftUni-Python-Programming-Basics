days = int(input())
hours = int(input())

hourly_pay = 0
daily_pay = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            hourly_pay += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            hourly_pay += 1.25
        else:
            hourly_pay += 1
    print(f"Day: {day} - {hourly_pay:.2f} leva")
    daily_pay += hourly_pay
    hourly_pay = 0
print(f'Total: {daily_pay:.2f} leva')