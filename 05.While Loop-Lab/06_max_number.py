import sys
max_num = -sys.maxsize

while True:
    command = input()

    if str(command) == 'Stop':
        break
    elif int(command) > max_num:
        max_num = int(command)

print(max_num)