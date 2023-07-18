expected_income = int(input())

i = 0
cash = 0
card = 0

cash_nr = 0
card_nr = 0
error = False
ended = False

while expected_income > 0:
    item_price = input()
    i += 1
    if item_price == 'End':
        ended = True
        break
    elif i % 2 == 0:
        if int(item_price) < 10:
            error = True
        else:
            card_nr += 1
            card += int(item_price)
            expected_income -= int(item_price)
    else:
        if int(item_price) > 100:
            error = True
        else:
            cash_nr += 1
            cash += int(item_price)
            expected_income -= int(item_price)

    if error:
        print('Error in transaction!')
    else:
        print('Product sold!')

    error = False

if ended:
    print('Failed to collect required money for charity.')
else:
    print(f'Average CS: {(cash/cash_nr):.2f}')
    print(f'Average CC: {(card/card_nr):.2f}')