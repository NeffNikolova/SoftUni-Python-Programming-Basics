from sys import maxsize

n = int(input())

max_num = -maxsize
sum = 0

for _ in range (n):
    number = int(input())
    sum += number
    if number > max_num:
        max_num = number

diff = abs(max_num-sum+max_num)

if sum - max_num == max_num:
    print('Yes')
    print(f'Sum = {sum-max_num}')
else:
    print('No')
    print(f'Diff = {diff}')
