width = int(input())
length = int(input())
height = int(input())

space = width * length * height


out_of_space = False

while space > 0:
    boxes = input()

    if boxes.lower() == 'done':
        out_of_space = True
        break
    space -= int(boxes)

if space <= 0:
    print(f'No more free space! You need {abs(space)} Cubic meters more.')
else:
    print(f'{space} Cubic meters left.')
