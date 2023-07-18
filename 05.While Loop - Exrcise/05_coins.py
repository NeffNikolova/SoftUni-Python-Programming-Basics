change = float(input())

coins_counter = 0
change *= 100
while change > 0:
    if change // 200 > 0:
        coins_counter += change // 200
        change -= ((change // 200) * 200)
    elif change // 100 > 0:
        coins_counter += change // 100
        change -= ((change // 100) * 100)
    elif change // 50 > 0:
        coins_counter += change // 50
        change -= ((change // 50) * 50)
    elif change // 20 > 0:
        coins_counter += change // 20
        change -= ((change // 20) * 20)
    elif change // 20 > 0:
        coins_counter += change // 20
        change -= ((change // 20) * 20)
    elif change // 10 > 0:
        coins_counter += change // 10
        change -= ((change // 10) * 10)
    elif change // 5 > 0:
        coins_counter += change // 5
        change -= ((change // 5) * 5)
    elif change // 2 > 0:
        coins_counter += change // 2
        change -= ((change // 2) * 2)
    else:
        coins_counter += change
        change = 0

print(f'{coins_counter:.0f}')