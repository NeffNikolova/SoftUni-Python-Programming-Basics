voucher_value = int(input())

purchase_price = 0
tickets = 0
other = 0

while voucher_value > 0:
    purchase = input()
    if purchase == 'End':
        break
    elif len(purchase) > 8:
        purchase_price = ord(purchase[0]) + ord(purchase[1])
        if voucher_value >= purchase_price:
            voucher_value -= purchase_price
            tickets += 1
        else:
            break
    elif len(purchase) <= 8:
        purchase_price = ord(purchase[0])
        if voucher_value >= purchase_price:
            voucher_value -= purchase_price
            other += 1
        else:
            break
print(tickets)
print(other)