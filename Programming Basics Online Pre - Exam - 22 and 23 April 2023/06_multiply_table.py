number = int(input())

number = str(number)

first_digit = 0
second_digit = 0
third_digit = 0

for index, digit in enumerate(number):
    if index == 0:
        first_digit = digit
    elif index == 1:
        second_digit = digit
    elif index == 2:
        third_digit = digit

    for third in range(1, int(third_digit) + 1):
        for second in range(1, int(second_digit) +1):
            for first in range(1, int(first_digit) + 1):
                result = first * second * third
                print(f'{third} * {second} * {first} = {result};')