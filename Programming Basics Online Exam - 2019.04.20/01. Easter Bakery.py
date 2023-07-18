flour_price = float(input())
flour_kgs = float(input())
sugar_kg = float(input())
eggs_nr = int(input())
yeast_packs_nr = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.10
yeast_pack_price = sugar_price * 0.20

expences = (flour_price * flour_kgs) + (sugar_price * sugar_kg) + (eggs_nr * eggs_price) + (yeast_packs_nr * yeast_pack_price)

print(f'{expences:.2f}')