from math import floor, ceil

magnolia_nr = int(input())
hyacinth_nr = int(input())
rose_nr = int(input())
cactus_nr = int(input())
present_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4 #зюмбюл
rose_price = 3.50
cactus_price = 8
difference = 0

earnings = 0.95 * ((magnolia_price * magnolia_nr) + (hyacinth_price * hyacinth_nr) + (rose_price * rose_nr) + (cactus_price * cactus_nr))

if earnings >= present_price:
    difference = floor(earnings - present_price)
    print(f'She is left with {difference} leva.')
else:
    difference = ceil(present_price - earnings)
    print(f'She will have to borrow {difference} leva.')
