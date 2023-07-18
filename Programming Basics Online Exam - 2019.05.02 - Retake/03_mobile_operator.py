contract_length = input()
contract_type = input()
internet = input()
months = int(input())

internet_price = 0
monthly_price = 0

if contract_type == 'Small':
    if contract_length == 'one':
        monthly_price = 9.98
    if contract_length == 'two':
        monthly_price = 8.58
elif contract_type == 'Middle':
    if contract_length == 'one':
        monthly_price = 18.99
    if contract_length == 'two':
        monthly_price = 17.09
elif contract_type == 'Large':
    if contract_length == 'one':
        monthly_price = 25.98
    if contract_length == 'two':
        monthly_price = 23.59
elif contract_type == 'ExtraLarge':
    if contract_length == 'one':
        monthly_price = 35.99
    if contract_length == 'two':
        monthly_price = 31.79

if internet == 'yes':
    if monthly_price <= 10:
        internet_price = 5.50
    if 10 < monthly_price <= 30:
        internet_price = 4.35
    if monthly_price > 30:
        internet_price = 3.85

price_all = (monthly_price + internet_price) * months

if contract_length == 'two':
    price_all *= 0.9625

print(f'{price_all:.2f} lv.')