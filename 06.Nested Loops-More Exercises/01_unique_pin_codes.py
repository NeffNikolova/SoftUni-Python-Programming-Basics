a_max = int(input())
b_max = int(input())
c_max = int(input())

dividers = 0

for a in range(1, a_max + 1):
    if a % 2 == 0:
        for b in range(1, b_max + 1):
            if 2 <= b <= 7:
                for n in range(2, b + 1):
                    if b % n == 0:
                        dividers += 1

                if dividers == 1:
                    dividers = 0
                    for c in range(1, c_max + 1):
                        if c % 2 == 0:
                            print(f'{a} {b} {c}')
                else:
                    dividers = 0

