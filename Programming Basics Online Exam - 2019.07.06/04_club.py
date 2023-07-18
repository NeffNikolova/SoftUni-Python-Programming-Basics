desired_profit = float(input())

cocktail_price = 0
order_price = 0
income = 0

while desired_profit > 0:
    cocktail_name = input()

    if cocktail_name == 'Party!':
        print(f"We need {desired_profit:.2f} leva more.")
        break
    else:
        nr_cocktails = int(input())
        cocktail_price = len(cocktail_name)
        order_price = cocktail_price * nr_cocktails
        if order_price % 2 != 0:
            order_price *= 0.75
        desired_profit -= order_price
        income += order_price


if desired_profit <= 0:
    print(f"Target acquired.")

print(f'Club income - {income:.2f} leva.')
