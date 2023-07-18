free_days = int(input())
norm_play_mins = 30000
work_days = 365 - free_days
difference = 0
difference_hr = 0
difference_min = 0

play_per_year_min = free_days * 127 + work_days * 63

if play_per_year_min > norm_play_mins:
    difference = play_per_year_min - norm_play_mins
    difference_hr = difference // 60
    difference_min = difference % 60
    print('Tom will run away')
    print(f'{difference_hr} hours and {difference_min} minutes more for play')
else:
    difference = norm_play_mins - play_per_year_min
    difference_hr = difference // 60
    difference_min = difference % 60
    print('Tom sleeps well')
    print(f'{difference_hr} hours and {difference_min} minutes less for play')



