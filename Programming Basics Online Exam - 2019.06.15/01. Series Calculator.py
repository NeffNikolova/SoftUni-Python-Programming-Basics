from math import ceil

series_name = input()
seasons = int(input())
episodes_in_season = int(input())
episode_time_no_commercials = float(input())

episode_time = episode_time_no_commercials * 1.20
one_season_time = (episodes_in_season * episode_time) + 10
all_seasons_time = ceil(one_season_time * seasons)

print(f'Total time needed to watch the {series_name} series is {all_seasons_time} minutes.')