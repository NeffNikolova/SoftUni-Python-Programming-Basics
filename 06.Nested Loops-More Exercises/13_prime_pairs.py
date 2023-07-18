start_ab = int(input())
start_cd = int(input())
dif_ending_ab = int(input())
dif_ending_cd = int(input())

dividers_ab = 0
dividers_cd = 0

for ab in range(start_ab, start_ab + dif_ending_ab + 1):
    for n in range(2, ab + 1):
        if ab % n == 0:
            dividers_ab += 1
    if dividers_ab == 1:
        for cd in range(start_cd, start_cd + dif_ending_cd + 1):
            for m in range(2, cd + 1):
                if cd % m == 0:
                    dividers_cd += 1
            if dividers_cd == 1:
                dividers_cd = 0
                dividers_ab = 0
                print(f'{ab}{cd}')
            else:
                dividers_cd = 0
                dividers_ab = 0
    else:
        dividers_ab = 0



