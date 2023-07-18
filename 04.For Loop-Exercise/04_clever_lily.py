lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

money = 0
nr_toys = 0
count_even_bd = 0
current_money = 0


for i in range (1,lily_age + 1):
    if i % 2 != 0:
        nr_toys += 1
    elif i % 2 == 0:
        count_even_bd += 1
        current_money = count_even_bd * 10
        money += current_money

money -= count_even_bd

toy_money = nr_toys * toy_price
all_money = toy_money + money

diff = abs(all_money - washer_price)

if all_money >= washer_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')


