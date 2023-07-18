price_skumria = float(input())
price_caca = float(input())
palamud_kgs = float(input())
safrid_kgs = float(input())
midi_kgs = int(input())

price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8
price_midi = 7.5

funds_needed = (price_palamud * palamud_kgs) + (price_safrid * safrid_kgs) + (price_midi * midi_kgs)

print(f'{funds_needed:.2f}')

