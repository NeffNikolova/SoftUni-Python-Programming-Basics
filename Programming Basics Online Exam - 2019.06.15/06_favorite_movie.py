movie_title = input()

max_pts = 0
max_title = ''

current_pts = 0
current_lowkey = 0
current_capitals = 0
movies = 0

while movie_title != 'STOP':
    movies += 1
    for n in range(len(movie_title)):
        current_pts += ord(movie_title[n])

        if 65 <= ord(movie_title[n]) <= 90:
            current_capitals += 1
        elif 97 <= ord(movie_title[n]) <= 122:
            current_lowkey += 1

    current_pts -= ((current_capitals*len(movie_title)) + (current_lowkey*2*len(movie_title)))

    if current_pts > max_pts:
        max_pts = current_pts
        max_title = movie_title

    if movies == 7:
        print(f"The limit is reached.")
        break

    current_pts = 0
    current_lowkey = 0
    current_capitals = 0
    movie_title = input()

print(f"The best movie for you is {max_title} with {max_pts} ASCII sum.")