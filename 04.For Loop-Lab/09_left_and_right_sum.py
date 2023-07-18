n = int(input())

left_sum = 0
right_sum = 0

for i in range(n*2):
    number = int(input())

    if i < (n*2)/2:
        left_sum += number
    else:
        right_sum += number

diff = abs(left_sum-right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')

