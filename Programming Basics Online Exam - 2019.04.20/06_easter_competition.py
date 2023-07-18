breads_nr = int(input())

points = 0
max_points = 0
max_baker = ''

for bread in range(breads_nr):
    baker_name = input()
    current_points = input()
    while current_points != 'Stop':
        current_points = int(current_points)
        points += current_points
        current_points = input()

    if points > max_points:
        max_points = points
        max_baker = baker_name
        print(f"{baker_name} has {points} points.")
        print(f"{baker_name} is the new number 1!")
    else:
        print(f"{baker_name} has {points} points.")
    points = 0

print(f"{max_baker} won competition with {max_points} points!")


