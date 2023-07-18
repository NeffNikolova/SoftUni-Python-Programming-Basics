nr_guests = int(input())
covert_price = float(input())
budget = float(input())

cake_price = budget * 0.10

if 10 <= nr_guests <= 15:
    covert_price *= 0.85
elif 15 <= nr_guests <= 20:
    covert_price *= 0.80
elif nr_guests > 20:
    covert_price *= 0.75

needed_funds = covert_price * nr_guests + cake_price

diff = abs(budget - needed_funds)

if needed_funds <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')

