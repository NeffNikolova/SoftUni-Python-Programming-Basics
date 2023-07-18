sum_1 = int(input())

sum_2 = 0

while True:
    num = int(input())

    sum_2 += num

    if sum_2 >= sum_1:
        print(sum_2)
        break