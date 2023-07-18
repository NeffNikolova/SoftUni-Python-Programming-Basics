player_name = input()

remaining_points = 301
current_points = 0
succ_shots = 0
unsucc_shots = 0

while True:
    action = input()

    if action == 'Retire':
        break

    points = int(input())

    if action == 'Single':
        current_points = (points * 1)
        if current_points > remaining_points:
            unsucc_shots += 1
            continue
        else:
            remaining_points -= current_points
            succ_shots += 1
    elif action == 'Double':
        current_points = (points * 2)
        if current_points > remaining_points:
            unsucc_shots += 1
            continue
        else:
            remaining_points -= current_points
            succ_shots += 1
    elif action == 'Triple':
        current_points = (points * 3)
        if current_points > remaining_points:
            unsucc_shots += 1
            continue
        else:
            remaining_points -= current_points
            succ_shots += 1

    if remaining_points > 0:
        continue
    else:
        break

if remaining_points == 0:
    print(f"{player_name} won the leg with {succ_shots} shots.")
else:
    print(f"{player_name} retired after {unsucc_shots} unsuccessful shots.")


