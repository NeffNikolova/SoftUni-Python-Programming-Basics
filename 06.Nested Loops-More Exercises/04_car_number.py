beginning = int(input())
ending = int(input())

for a in range(beginning, ending + 1):
    for b in range(beginning, ending + 1):
        for c in range(beginning, ending + 1):
            if (b + c) % 2 == 0:
                for d in range(beginning, ending + 1):
                    if a > d:
                        if (a % 2 == 0 and d % 2 != 0) or (a % 2 != 0 and d % 2 == 0):
                            print(f'{a}{b}{c}{d}', end=' ')

