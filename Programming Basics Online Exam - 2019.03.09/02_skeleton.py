control_minutes_100m = int(input())
control_seconds_100m = int(input())
slide_lenght = float(input())
secs_100m = int(input())

speeding_time = (slide_lenght / 120) * 2.5

control_seconds_100 = (control_minutes_100m * 60) + control_seconds_100m

Marin_time = (slide_lenght / 100) * secs_100m - speeding_time

#control_seconds_all = control_seconds_100 * (slide_lenght / 100)

diff = abs(Marin_time - control_seconds_100)

if Marin_time <= control_seconds_100:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {Marin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {diff:.3f} second slower.')