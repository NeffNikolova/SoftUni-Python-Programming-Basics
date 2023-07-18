from math import floor

record_sec = float(input())
distance_m = float(input())
time_per_m = float(input())

additional_delay = floor(distance_m / 50) * 30

Georgi_time = (distance_m * time_per_m) + additional_delay

diff =  Georgi_time - record_sec

if Georgi_time < record_sec:
    print(f'Yes! The new record is {Georgi_time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')

