us1, empty1, them1 = input()
us2, empty2, them2 = input()
us3, empty3, them3 = input()

games_won = 0
games_lost = 0
games_drawn = 0

if us1 > them1:
    games_won += 1
elif us1 == them1:
    games_drawn += 1
elif us1 < them1:
    games_lost += 1

if us2 > them2:
    games_won += 1
elif us2 == them2:
    games_drawn += 1
elif us2 < them2:
    games_lost += 1

if us3 > them3:
    games_won += 1
elif us3 == them3:
    games_drawn += 1
elif us3 < them3:
    games_lost += 1

print(f'Team won {games_won} games.')
print(f'Team lost {games_lost} games.')
print(f'Drawn games: {games_drawn}')
