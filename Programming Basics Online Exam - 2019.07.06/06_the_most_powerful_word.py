word = input()

points = 0
most_points = 0
most_powerful_word = ''

while word != 'End of words':
    for n in range(len(word)):
        points += ord(word[n])

    if word[0] in 'aeiouyAEIOUY':
        points *= len(word)
    else:
        points /= len(word)

    if points >= most_points:
        most_points = points
        most_powerful_word = word

    points = 0
    word = input()

print(f"The most powerful word is {most_powerful_word} - {most_points}" )