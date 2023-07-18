movie = input()
salon_type = input()
tickets = int(input())

income = 0

if movie.lower() == 'a star is born':
    if salon_type.lower() == 'normal':
        income = tickets * 7.50
    elif salon_type.lower() == 'luxury':
        income = tickets * 10.50
    elif salon_type.lower() == 'ultra luxury':
        income = tickets * 13.50
elif movie.lower() == 'bohemian rhapsody':
    if salon_type.lower() == 'normal':
        income = tickets * 7.35
    elif salon_type.lower() == 'luxury':
        income = tickets * 9.45
    elif salon_type.lower() == 'ultra luxury':
        income = tickets * 12.75
elif movie.lower() == 'green book':
    if salon_type.lower() == 'normal':
        income = tickets * 8.15
    elif salon_type.lower() == 'luxury':
        income = tickets * 10.25
    elif salon_type.lower() == 'ultra luxury':
        income = tickets * 13.25
elif movie.lower() == 'the favourite':
    if salon_type.lower() == 'normal':
        income = tickets * 8.75
    elif salon_type.lower() == 'luxury':
        income = tickets * 11.55
    elif salon_type.lower() == 'ultra luxury':
        income = tickets * 13.95

print(f'{movie} -> {income:.2f} lv.')