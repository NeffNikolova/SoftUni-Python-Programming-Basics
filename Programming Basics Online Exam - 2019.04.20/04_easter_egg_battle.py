eggs_1 = int(input())
eggs_2 = int(input())

end = False

winner = input()
while winner != 'End':
    if winner == 'one':
        eggs_2 -= 1
    elif winner == 'two':
        eggs_1 -= 1

    if  eggs_1 == 0 or eggs_2 == 0:
        break
    else:
        winner = input()
else:
    end = True

if end:
    print(f"Player one has {eggs_1} eggs left.")
    print(f"Player two has {eggs_2} eggs left.")
elif eggs_1 == 0:
    print(f"Player one is out of eggs. Player two has {eggs_2} eggs left.")
elif eggs_2 == 0:
    print(f"Player two is out of eggs. Player one has {eggs_1} eggs left.")