price_per_sqm = 7.61
discount_factor = 0.18
discounted_price_factor = 1-0.18
area = float(input())
price = price_per_sqm * area
final_price = round(price * discounted_price_factor, 2)
discount = round(discount_factor * price, 2)
print('The final price is: ' + str(final_price) + ' lv.')
print('The discount is: ' + str(discount) + ' lv.')
