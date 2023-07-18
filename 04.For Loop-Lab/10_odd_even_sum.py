n = int(input())

odd_sum = 0
even_sum = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

diff = abs(even_sum-odd_sum)

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {diff}')