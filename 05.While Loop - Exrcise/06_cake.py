cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width
stopped = False

while cake_pieces >= 0:
    cake_taken = input()

    if cake_taken.lower() == 'stop':
        stopped = True
        break

    cake_pieces -= int(cake_taken)

if stopped and cake_pieces >= 0:
    print(f"{cake_pieces} pieces are left.")
elif cake_pieces < 0:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
