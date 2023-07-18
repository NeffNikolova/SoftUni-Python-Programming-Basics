days = int(input())
accommodation = input()
score = input()

nights = days - 1

price_stay = 0

if accommodation == 'room for one person':
    price_stay = nights * 18
elif accommodation == 'apartment':
    price_stay = nights * 25
    if days < 10:
        price_stay *= 0.70
    elif 10 <= days <= 15:
        price_stay *= 0.65
    elif days > 15:
        price_stay *= 0.50
elif accommodation == 'president apartment':
    price_stay = nights * 35
    if days < 10:
        price_stay *= 0.90
    elif 10 <= days <= 15:
        price_stay *= 0.85
    elif days > 15:
        price_stay *= 0.80

if score == 'positive':
    price_stay *= 1.25
else:
    price_stay *= 0.90

print(f'{price_stay:.2f}')