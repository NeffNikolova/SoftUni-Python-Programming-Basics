kilometers = int(input())
day_night = input()

taxi_starting = 0.70
taxi_day_km = 0.79
taxi_night_km = 0.90

bus_km = 0.09
train_km = 0.06

travel_price = 0

if kilometers >= 100:
    travel_price = train_km * kilometers
elif kilometers >= 20:
    travel_price = bus_km * kilometers
elif day_night == 'day':
    travel_price = taxi_starting + (taxi_day_km * kilometers)
else:
    travel_price = taxi_starting + (taxi_night_km * kilometers)

print(f'{travel_price:.2f}')