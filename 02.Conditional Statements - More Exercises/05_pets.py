from math import floor, ceil

days_missing = int(input())
food_kg_left = int(input())
dog_daily = float(input())
cat_daily = float(input())
turtle_daily = float(input()) / 1000

difference = 0

food_needed = days_missing * (dog_daily + cat_daily + turtle_daily)

if food_needed <= food_kg_left:
    difference = floor(food_kg_left - food_needed)
    print(f'{difference} kilos of food left.')
else:
    difference = ceil(food_needed - food_kg_left)
    print(f'{difference} more kilos of food are needed.')
