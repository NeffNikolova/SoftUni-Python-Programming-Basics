kozunak_nr = int(input())
eggs_nr = int(input())
cookies_kg = int(input())

kozunak_price = 3.20
eggs_price = 4.35 # na kora 12 qica
cookies_price = 5.40 # na kg
egg_paint = 0.15 # na qice

expences = (kozunak_nr * kozunak_price) + (cookies_kg * cookies_price) + (eggs_nr * eggs_price) + (eggs_nr * 12 * egg_paint)

print(f'{expences:.2f}')