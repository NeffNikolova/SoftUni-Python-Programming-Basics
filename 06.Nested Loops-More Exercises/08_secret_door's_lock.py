hundrets_max = int(input())
tens_max = int(input())
ones_max = int(input())

dividers = 0

for a in range(1,hundrets_max + 1):
    for b in range(1, tens_max + 1):
        for c in range(1, ones_max + 1):
            if a % 2 == 0 and c % 2 == 0:
                for n in range(2, b + 1):
                    if b % n == 0 and 2 <= b <= 7:
                        dividers += 1
                if dividers == 1:
                    dividers = 0
                    print(f'{a} {b} {c}')
                else:
                    dividers = 0

