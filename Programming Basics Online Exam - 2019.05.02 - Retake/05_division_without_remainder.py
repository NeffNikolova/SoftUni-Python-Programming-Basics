numbers = int(input())

p_2 = 0
p_3 = 0
p_4 = 0

for _ in range(numbers):
    num = int(input())

    if num % 2 == 0:
        p_2 += 1
    if num % 3 == 0:
        p_3 += 1
    if num % 4 == 0:
        p_4 += 1


p_2 *= (100/numbers)
p_3 *= (100/numbers)
p_4 *= (100/numbers)

print(f'{p_2:.2f}%')
print(f'{p_3:.2f}%')
print(f'{p_4:.2f}%')
