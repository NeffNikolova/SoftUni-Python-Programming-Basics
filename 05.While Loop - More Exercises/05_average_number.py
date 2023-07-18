n = int(input())

nr = 0
sum = 0

for _ in range(n):
    number = int(input())
    nr += 1
    sum += number

print(f'{(sum/nr):.2f}')