egg_size = input()
egg_color = input()
eggs_nr = int(input())

income = 0
price_egg = 0

if egg_color == 'Red':
    if egg_size == 'Large':
        price_egg = 16
    elif egg_size == 'Medium':
        price_egg = 13
    elif egg_size == 'Small':
        price_egg = 9
elif egg_color == 'Green':
    if egg_size == 'Large':
        price_egg = 12
    elif egg_size == 'Medium':
        price_egg = 9
    elif egg_size == 'Small':
        price_egg = 8
elif egg_color == 'Yellow':
    if egg_size == 'Large':
        price_egg = 9
    elif egg_size == 'Medium':
        price_egg = 7
    elif egg_size == 'Small':
        price_egg = 5

income = eggs_nr * price_egg * 0.65
print(f'{income:.2f} leva.')
