juniors = int(input())
seniors = int(input())
trace = input()

juniors_ticket = 0
seniors_ticket = 0

if trace == 'trail':
    juniors_ticket = 5.50
    seniors_ticket = 7
elif trace == 'cross-country':
    juniors_ticket = 8
    seniors_ticket = 9.50
    if juniors + seniors >= 50:
        juniors_ticket *= 0.75
        seniors_ticket *= 0.75
elif trace == 'downhill':
    juniors_ticket = 12.25
    seniors_ticket = 13.75
elif trace == 'road':
    juniors_ticket = 20
    seniors_ticket = 21.50

donations = (juniors * juniors_ticket + seniors * seniors_ticket) * 0.95

print(f'{donations:.2f}')