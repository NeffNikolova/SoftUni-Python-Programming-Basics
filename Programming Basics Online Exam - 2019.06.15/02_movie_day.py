shooting_time = int(input())
scenes_nr = int(input())
time_per_scene = int(input())

terrain_preparation = shooting_time * 0.15

needed_time = time_per_scene * scenes_nr + terrain_preparation

diff = abs(needed_time - shooting_time)

if shooting_time >= needed_time:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')