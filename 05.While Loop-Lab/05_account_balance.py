deposit = input()

total = 0
increase = 0

while deposit != 'NoMoreMoney':
    if float(deposit) < 0:
        print('Invalid operation!')
        break
    else:
        increase = float(deposit)
        print(f'Increase: {increase:.2f}')
        total += increase
        deposit = input()
print(f'Total: {total:.2f}')
