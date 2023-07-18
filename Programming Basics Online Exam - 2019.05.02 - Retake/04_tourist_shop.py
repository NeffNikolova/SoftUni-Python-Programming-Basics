budget = float(input())

stop = False
nr_products = 0
price_all = 0
while True:
    product = input()

    if product == 'Stop':
        stop = True
        break
    else:
        product_price = float(input())
        nr_products += 1
        if nr_products % 3 == 0:
            product_price *= 0.5
            budget -= product_price
            price_all += product_price
        else:
            budget -= product_price
            price_all += product_price

        if budget < 0:
            nr_products -= 1
            break

if stop:
    print(f"You bought {nr_products} products for {price_all:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")