control_nr = int(input())

numbers = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == control_nr:
                    print(f'{a}{b}{c}{d}', end=' ')
                    numbers += 1
                    if numbers == 4:
                        password = str(a)+str(b)+str(c)+str(d)
                    else:
                        continue

if numbers >= 4:
    print()
    print(f'Password: {password}')
elif 0 < numbers < 4:
    print()
    print('No!')
else:
    print('No!')
