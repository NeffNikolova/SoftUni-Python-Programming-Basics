seats = int(input())

income = 0
current_income = 0

full = False

while True:
    group_size = input()

    if group_size == 'Movie time!':
        break
    else:
        group_size = int(group_size)
        if group_size > seats:
            full = True
            break
        else:
            current_income = group_size * 5
            seats -= group_size
            if group_size % 3 == 0:
                current_income -= 5
                income += current_income
            else:
                income += current_income

if full:
    print("The cinema is full.")
else:
    print(f"There are {seats} seats left in the cinema.")

print(f'Cinema income - {income} lv.')