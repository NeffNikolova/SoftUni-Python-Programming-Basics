record_sec = float(input())
distance_m = float(input())
time_sec_1m = float(input())

slow_factor = distance_m // 15
slow_time = slow_factor * 12.5
missing_secs = 0

time_ivan = (distance_m * time_sec_1m)  + slow_time

if time_ivan < record_sec:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    missing_secs = time_ivan - record_sec
    print(f'No, he failed! He was {missing_secs:.2f} seconds slower.')