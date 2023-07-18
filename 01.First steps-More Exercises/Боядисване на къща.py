x = float(input())
y = float(input())
h = float(input())

litre_green_paint_coverage = 3.4
litre_red_paint_coverage = 4.3

area_front_n_back = 2 * (x * x) - (1.2 * 2)
area_sides = 2 * (x * y) - (2 * (1.5 * 1.5))
area_roof = (x * h) + 2 * (x * y)

red_paint_needed = area_roof / litre_red_paint_coverage
green_paint_needed = (area_sides + area_front_n_back) / litre_green_paint_coverage

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
