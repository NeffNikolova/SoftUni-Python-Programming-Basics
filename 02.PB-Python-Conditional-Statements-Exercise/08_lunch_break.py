from math import ceil

series_name = input()
episode_lenght = int(input())
break_lenght = int(input())

difference = 0

lunch_time = 1/8 * break_lenght
calm_time = 1/4 * break_lenght

rest_break = break_lenght - lunch_time - calm_time

if episode_lenght <= rest_break:
    difference = ceil(rest_break - episode_lenght)
    print(f'You have enough time to watch {series_name} and left with {difference} minutes free time.')
else:
    difference = ceil(episode_lenght - rest_break)
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")
