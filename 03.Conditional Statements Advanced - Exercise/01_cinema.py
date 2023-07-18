projection = input()
rows = int(input())
columns = int(input())
projection = projection.lower()

income = 0

if projection == 'premiere':
    income = rows * columns * 12
elif projection == 'normal':
    income = rows * columns * 7.50
elif projection == 'discount':
    income = rows * columns * 5

print(f'{income:.2f} leva')