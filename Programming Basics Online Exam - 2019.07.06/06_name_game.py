name = input()

points = 0
winner_name = ''
winner_points = 0

while name != 'Stop':
    for n in range(len(name)):
        number = int(input())
        if ord(name[n]) == number:
            points += 10
        else:
            points += 2

        if points >= winner_points:
            winner_points = points
            winner_name = name

    points = 0
    name = input()

print(f'The winner is {winner_name} with {winner_points} points!')
