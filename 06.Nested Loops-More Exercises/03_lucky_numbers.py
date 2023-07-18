N = int(input())

ab = 0
cd = 0

for a in range(1, 10):
    for b in range(1, 10):
        ab = a + b
        for c in range(1, 10):
            for d in range(1, 10):
                cd = c + d
                if ab == cd and N % ab == 0:
                    print(f'{a}{b}{c}{d}', end=' ')
