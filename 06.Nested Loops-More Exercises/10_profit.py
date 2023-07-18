ones = int(input())
twos = int(input())
fives = int(input())
income = int(input())

for o in range(ones+1):
    for t in range(twos + 1):
        for f in range(fives + 1):
            if o + t*2 + f*5 == income:
                print(f"{o} * 1 lv. + {t} * 2 lv. + {f} * 5 lv. = {income} lv.")