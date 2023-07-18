from math import ceil

wall_height = int(input())
wall_length = int(input())
excluded_p = int(input()) / 100

area_to_paint = ceil(wall_height * wall_length * 4) * (1 - excluded_p)

while True:
    paint = input()

    if paint == 'Tired!':
        print(f'{area_to_paint:.0f} quadratic m left.')
        break
    else:
        paint = int(paint)
        area_to_paint -= paint
        if area_to_paint <= 0:
            break

if area_to_paint < 0:
    print(f'All walls are painted and you have {abs(area_to_paint):.0f} l paint left!')
elif area_to_paint == 0:
    print(f"All walls are painted! Great job, Pesho!")





