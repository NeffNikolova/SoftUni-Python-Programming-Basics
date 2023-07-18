food_bought = int(input())
food_bought *= 1000

eaten = input()
while eaten != 'Adopted':
    eaten = int(eaten)
    food_bought -= eaten
    eaten = input()

if food_bought >= 0:
    print(f"Food is enough! Leftovers: {food_bought} grams.")
else:
    print(f'Food is not enough. You need {abs(food_bought)} grams more.')
