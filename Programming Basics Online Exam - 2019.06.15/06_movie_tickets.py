a1 = int(input())
a2 = int(input())
n = int(input())

for sym1 in range(a1, a2):
    for sym2 in range(1, n):
        for sym3 in range(1, int(n / 2)):
            if sym1 % 2 != 0 and (sym2 + sym3 + sym1) % 2 != 0:
                print(f'{chr(sym1)}-{sym2}{sym3}{sym1}')


