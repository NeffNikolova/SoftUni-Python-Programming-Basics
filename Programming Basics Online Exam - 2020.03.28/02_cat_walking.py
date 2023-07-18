minutes_walk_daily = int(input())
number_of_walks_daily = int(input())
calories_daily = int(input())

burned_calories = minutes_walk_daily * 5 * number_of_walks_daily

if burned_calories >= (calories_daily * 0.50):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: '
          f'{burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: '
          f'{burned_calories}.')
