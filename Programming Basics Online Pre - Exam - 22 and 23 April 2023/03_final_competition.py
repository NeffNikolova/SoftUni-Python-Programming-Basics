dancers = int(input())
points = float(input())
season = input()
place = input()

price = 0

if place == 'Bulgaria':
    price = points * dancers
    if season == 'summer':
        price *= 0.95
    elif season == 'winter':
        price *= 0.92
elif place == 'Abroad':
    price = 1.5 * (points * dancers)
    if season == 'summer':
        price *= 0.90
    elif season == 'winter':
        price *= 0.85

donation = 0.75 * price
per_dancer = (price - donation) / dancers

print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {per_dancer:.2f}")