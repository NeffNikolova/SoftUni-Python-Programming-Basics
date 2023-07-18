max_num = int(input())

num = 1
while True:
    if num > max_num:
        break

    print(num)
    num = 2 * num + 1