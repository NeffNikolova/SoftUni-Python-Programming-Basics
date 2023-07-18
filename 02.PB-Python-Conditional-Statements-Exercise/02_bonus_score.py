beginning_points =  int(input())

if beginning_points <= 100:
    bonus_points = 5
elif 100 < beginning_points <= 1000:
    bonus_points = beginning_points * 0.2
else:
    bonus_points = beginning_points * 0.1

if beginning_points % 2 == 0:
    additional_points = 1
elif beginning_points % 10 == 5:
        additional_points = 2
else:
    additional_points = 0

total_points = beginning_points + bonus_points + additional_points

print(bonus_points + additional_points)
print(total_points)

