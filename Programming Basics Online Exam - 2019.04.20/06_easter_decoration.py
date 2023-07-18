customers = int(input())

purchase_nr = 0
price = 0
avg_price = 0

for customer in range(customers):
    purchase = input()
    while purchase != 'Finish':
        purchase_nr += 1

        if purchase == 'basket':
            price += 1.50
        elif purchase == 'wreath':
            price += 3.80
        elif purchase == 'chocolate bunny':
            price += 7.00
        purchase = input()

    else:
        if purchase_nr % 2 == 0:
            price *= 0.80

        print(f"You purchased {purchase_nr} items for {price:.2f} leva.")

    avg_price += price
    purchase_nr = 0
    price = 0

print(f'Average bill per client is: {(avg_price/customers):.2f} leva.')

