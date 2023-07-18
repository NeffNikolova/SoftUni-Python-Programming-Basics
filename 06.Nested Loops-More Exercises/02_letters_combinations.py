beginning = input()
ending = input()
exclude = input()

number = 0

for first in range(ord(beginning), ord(ending) + 1):
    for second in range(ord(beginning), ord(ending) + 1):
        for third in range(ord(beginning), ord(ending) + 1):
            if first != ord(exclude) and second != ord(exclude) and third != ord(exclude):
                number += 1
                print(f'{chr(first)}{chr(second)}{chr(third)}', end=' ')
print(number)