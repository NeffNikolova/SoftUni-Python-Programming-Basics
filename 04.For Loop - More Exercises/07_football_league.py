stadium_capacity = int(input())
fans_nr = int(input())

A = 0
B = 0
V = 0
G = 0

for i in range(fans_nr):
    current_sector = input()

    if current_sector == 'A':
        A += 1
    elif current_sector == 'B':
        B += 1
    elif current_sector == 'V':
        V += 1
    elif current_sector == 'G':
        G += 1

A_p = A / fans_nr * 100
B_p = B / fans_nr * 100
V_p = V / fans_nr * 100
G_p = G / fans_nr * 100
all_p = fans_nr / stadium_capacity * 100

print(f'{A_p:.2f}%')
print(f'{B_p:.2f}%')
print(f'{V_p:.2f}%')
print(f'{G_p:.2f}%')
print(f'{all_p:.2f}%')
