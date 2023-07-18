vegies_price_N = float(input())
fruit_price_M = float(input())

vegies_kgs = int(input())
fruit_kgs = int(input())

income_BGN =  (vegies_price_N * vegies_kgs) + (fruit_price_M * fruit_kgs)
income_EUR = income_BGN / 1.94

print(f'{income_EUR:.2f}')
