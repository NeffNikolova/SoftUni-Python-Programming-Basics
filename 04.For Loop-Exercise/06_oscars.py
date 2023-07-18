actor_name = input()
academy_points = float(input())
jury_nr = int(input())

all_points = 0
all_jury_points = 0

for i in range (jury_nr):
    jury_name = input()
    jury_points = float(input())

    all_jury_points = len(jury_name) * jury_points / 2
    academy_points += all_jury_points

    if academy_points >= 1250.5:
        break

diff = abs(academy_points - 1250.5)
if academy_points >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')


