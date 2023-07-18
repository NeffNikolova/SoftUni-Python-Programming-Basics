number = int(input())
counter = 1
reached = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if counter > number:
            reached = True
            break
        print(str(counter) + ' ', end='')
        counter += 1
    if reached:
        break
    print()
