nr_eggs = int(input())

n_red = 0
n_orange = 0
n_blue = 0
n_green = 0
max_eggs = 1
max_color = ''

for _ in range(nr_eggs):
    color = input()

    if color == 'red':
        n_red += 1
    elif color == 'orange':
        n_orange += 1
    elif color == 'blue':
        n_blue += 1
    elif color == 'green':
        n_green += 1

if n_red > max_eggs:
    max_eggs = n_red
    max_color = 'red'
if n_green > max_eggs:
    max_eggs = n_green
    max_color = 'green'
if n_blue > max_eggs:
    max_eggs = n_blue
    max_color = 'blue'
if n_orange > max_eggs:
    max_eggs = n_orange
    max_color = 'orange'

print(f"Red eggs: {n_red}")
print(f"Orange eggs: {n_orange}")
print(f"Blue eggs: {n_blue}")
print(f"Green eggs: {n_green}")
print(f"Max eggs: {max_eggs} -> {max_color}")
