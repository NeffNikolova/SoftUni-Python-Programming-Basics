from math import floor

nr_tournaments = int(input())
start_points = int(input())

final_points = start_points
nr_wins = 0

for i in range (nr_tournaments):
    stage = input()

    if stage == 'W':
        final_points += 2000
        nr_wins += 1
    elif stage == 'F':
        final_points += 1200
    elif stage == 'SF':
        final_points += 720

average_points = floor((final_points - start_points) / nr_tournaments)
p_wins = nr_wins / nr_tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{p_wins:.2f}%')
