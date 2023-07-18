strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = 0.50 * strawberries_price
oranges_price = 0.60 * raspberries_price
bananas_price = 0.20 * raspberries_price

expences = (strawberries_kg * strawberries_price) + (bananas_kg * bananas_price) + \
           (oranges_kg * oranges_price) + (raspberries_kg * raspberries_price)

print(f'{expences:.2f}')
