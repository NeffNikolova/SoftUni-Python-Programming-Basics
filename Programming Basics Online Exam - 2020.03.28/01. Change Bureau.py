nr_bitcoins = int(input())
nr_yuan = float(input())
commission = float(input()) / 100

bitcoin = 1168
yuan = 0.15
USD = 1.76
EUR = 1.95

BGN_from_bitcoins = nr_bitcoins * bitcoin
USD_from_yuan = nr_yuan * yuan
BGN_from_USD = USD_from_yuan * USD

BGN_total = BGN_from_bitcoins + BGN_from_USD

EUR_total = BGN_total / EUR

EUR_after_commission = EUR_total * (1 - commission)

print(f'{EUR_after_commission:.2f}')