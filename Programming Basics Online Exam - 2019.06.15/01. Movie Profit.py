movie_name = input()
show_days = int(input())
tickets_per_day = int(input())
ticket_price = float(input())
theater_percent = int(input()) / 100

total_income = show_days * (tickets_per_day * ticket_price)
moviemaker_income = total_income * ( 1 - theater_percent)

print(f'The profit from the movie {movie_name} is {moviemaker_income:.2f} lv.')