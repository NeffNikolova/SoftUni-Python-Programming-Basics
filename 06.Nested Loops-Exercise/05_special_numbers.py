number = int(input())

for a in range(1,10):
    if number % a == 0:
        for b in range(1,10):
            if number % b == 0:
                for c in range(1, 10):
                    if number % c == 0:
                        for d in range(1, 10):
                            if number % d == 0:
                                print(f'{a}{b}{c}{d}', end=' ')
