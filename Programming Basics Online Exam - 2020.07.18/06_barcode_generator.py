beginning = int(input())
ending = int(input())

for sym1 in range(beginning//1000, ending//1000 + 1):
    for sym2 in range((beginning//100)%10, (ending//100)%10 + 1):
        for sym3 in range(((beginning//10)%100)%10, (((ending//10)%100)%10) + 1):
            for sym4 in range(((beginning%1000)%100)%10, (((ending%1000)%100)%10 + 1)):
                if sym1 % 2 != 0 and sym2 % 2 != 0 and sym3 % 2 != 0 and sym4 % 2 != 0:
                    print(f'{sym1}{sym2}{sym3}{sym4}', end=' ')

