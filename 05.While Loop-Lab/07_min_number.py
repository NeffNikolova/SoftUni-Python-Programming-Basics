import sys
min_num = sys.maxsize

while True:
    command = input()

    if str(command) == 'Stop':
        break
    elif int(command) < min_num:
        min_num = int(command)

print(min_num)