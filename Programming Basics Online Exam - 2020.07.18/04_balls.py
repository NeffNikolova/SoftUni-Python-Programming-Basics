import math

nr_balls = int(input())

points = 0
n_red = 0
n_orange = 0
n_yellow = 0
n_white = 0
n_other = 0
n_black = 0
for _ in range(nr_balls):
    color = input()

    if color == 'red':
        points += 5
        n_red += 1
    elif color == 'orange':
        points += 10
        n_orange += 1
    elif color == 'yellow':
        points += 15
        n_yellow += 1
    elif color == 'white':
        points += 20
        n_white += 1
    elif color == 'black':
        points = math.floor(points/2)
        n_black += 1
    else:
        n_other += 1
        pass

print(f"Total points: {points}")
print(f"Red balls: {n_red}")
print(f"Orange balls: {n_orange}")
print(f"Yellow balls: {n_yellow}")
print(f"White balls: {n_white}")
print(f"Other colors picked: {n_other}")
print(f"Divides from black balls: {n_black}")
