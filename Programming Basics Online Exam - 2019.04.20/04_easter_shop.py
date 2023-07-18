eggs = int(input())

all_sold = 0
more = False

# while True:
#     command = input()
#     number = int(input())
#
#     if command == 'Close':
#         break
#     elif command == 'Buy':
#         if eggs >= number:
#             eggs -= number
#             all_sold += number
#         else:
#             more = True
#             break
#     elif command == 'Fill':
#         eggs += number

command = input()
while command != 'Close':
    number = int(input())

    if command == 'Buy':
        if eggs >= number:
            eggs -= number
            all_sold += number
        else:
            more = True
            break
    elif command == 'Fill':
        eggs += number

    if eggs >= 0:
        command = input()
    else:
        break

if more:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs}.")
else:
    print('Store is closed!')
    print(f'{all_sold} eggs sold.')