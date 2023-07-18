floors = int(input())
rooms = int(input())
index = ''

for floor in range(floors, 0, -1):
    if floor == floors:
        index = 'L'
    elif floor % 2 == 0:
        index = 'O'
    elif floor % 2 != 0:
        index = 'A'
    for room in range(rooms):
        print(f'{index}{floor}{room}', end=" ")
    print()


