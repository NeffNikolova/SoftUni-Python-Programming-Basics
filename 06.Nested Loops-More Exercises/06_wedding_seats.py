last_sector = input()
rows = int(input())
initial_seats = int(input())

nr_seats = 0

ending_sector = ord(last_sector)
for sector in range(65, ending_sector + 1):
    for row in range(1, rows+1):
        seats = initial_seats if row % 2 else initial_seats + 2
        for seat in range(97, 97 + seats):
            print(f'{chr(sector)}{row}{chr(seat)}')
            nr_seats += 1
    rows = rows + 1
    ending_sector += 1
print(nr_seats)