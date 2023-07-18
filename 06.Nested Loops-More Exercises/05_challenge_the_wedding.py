men_nr = int(input())
women_nr = int(input())
tables_nr = int(input())

combination = 0

for a in range(1, men_nr + 1):
    for b in range(1, women_nr + 1):
        combination += 1
        if combination <= tables_nr:
            print(f'({a} <-> {b})', end=' ')