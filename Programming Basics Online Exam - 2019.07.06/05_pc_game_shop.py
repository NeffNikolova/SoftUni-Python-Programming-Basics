sold_copies = int(input())

p_hearthstone = 0
p_fornite = 0
p_overwatch = 0
p_others = 0

for _ in range(sold_copies):
    game_name = input()

    if game_name == 'Hearthstone':
        p_hearthstone += 1
    elif game_name == 'Fornite':
        p_fornite += 1
    elif game_name == 'Overwatch':
        p_overwatch += 1
    else:
        p_others += 1

p_hearthstone *= (100/sold_copies)
p_fornite *= (100/sold_copies)
p_overwatch *= (100/sold_copies)
p_others *= (100/sold_copies)

print(f'Hearthstone - {p_hearthstone:.2f}%')
print(f'Fornite - {p_fornite:.2f}%')
print(f'Overwatch - {p_overwatch:.2f}%')
print(f'Others - {p_others:.2f}%')
