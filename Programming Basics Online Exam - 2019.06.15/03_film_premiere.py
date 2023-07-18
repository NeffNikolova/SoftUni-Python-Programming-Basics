movie = input()
option = input()
tickets = int(input())

expenses = 0

if movie.lower() == 'john wick':
    if option.lower() == 'drink':
        expenses = tickets * 12
    elif option.lower() == 'popcorn':
        expenses = tickets * 15
    elif option.lower() == 'menu':
        expenses = tickets * 19
elif movie.lower() == 'star wars':
    if option.lower() == 'drink':
        expenses = tickets * 18
        if tickets >= 4:
            expenses *= 0.70
    elif option.lower() == 'popcorn':
        expenses = tickets * 25
        if tickets >= 4:
            expenses *= 0.70
    elif option.lower() == 'menu':
        expenses = tickets * 30
        if tickets >= 4:
            expenses *= 0.70
elif movie.lower() == 'jumanji':
    if option.lower() == 'drink':
        expenses = tickets * 9
        if tickets == 2:
            expenses *= 0.85
    elif option.lower() == 'popcorn':
        expenses = tickets * 11
        if tickets == 2:
            expenses *= 0.85
    elif option.lower() == 'menu':
        expenses = tickets * 14
        if tickets == 2:
            expenses *= 0.85

print(f'Your bill is {expenses:.2f} leva.')

