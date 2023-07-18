club_name = input()
matches_played = int(input())

points = 0
nr_W = 0
nr_D = 0
nr_L = 0

for _ in range(matches_played):
    result = input()
    if result == 'W':
        points += 3
        nr_W += 1
    elif result == 'D':
        points += 1
        nr_D += 1
    elif result == 'L':
        nr_L += 1

if matches_played == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    print(f'{club_name} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {nr_W}')
    print(f'## D: {nr_D}')
    print(f'## L: {nr_L}')
    print(f'Win rate: {(nr_W/matches_played*100):.2f}%')
