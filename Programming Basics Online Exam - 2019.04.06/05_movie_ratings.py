import sys

movies_nr = int(input())
highest_rating = -sys.maxsize
highest_rating_name = ''
lowest_rating = sys.maxsize
lowest_rating_name = ''
rating_sum = 0

for _ in range(movies_nr):
    movie_name = input()
    movie_rating = float(input())

    rating_sum += movie_rating

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rating_name = movie_name
    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_name = movie_name

average_rating = rating_sum / movies_nr

print(f'{highest_rating_name} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rating_name} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')




