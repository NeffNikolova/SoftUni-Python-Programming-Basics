import sys
pairs_nr = int(input())

odd_sum = 0
even_sum = 0
diff = 0
max_diff = -sys.maxsize

for i in range(1, pairs_nr + 1):

    number1 = int(input())
    number2 = int(input())

    if i % 2 == 0:
        even_sum = number1 + number2
    elif i % 2 != 0:
        odd_sum = number1 + number2

    if i != 1 and abs(odd_sum - even_sum) > max_diff:
        max_diff = abs(odd_sum - even_sum)
    elif pairs_nr == 1 and abs(number1 - number2) > max_diff:
        max_diff = abs(number1 - number2)

if max_diff != -sys.maxsize and max_diff != 0:
    print(f'No, maxdiff={max_diff}')
else:
    print(f'Yes, value={odd_sum}')






