nr_groups = int(input())

p_musala = 0
p_monblan = 0
p_kilimanjaro = 0
p_k2 = 0
p_everest = 0
all_ppl = 0

for i in range(nr_groups):
    nr_ppl = int(input())

    if nr_ppl <= 5:
        p_musala += nr_ppl
    elif 6 <= nr_ppl <= 12:
        p_monblan += nr_ppl
    elif 13 <= nr_ppl <= 25:
        p_kilimanjaro += nr_ppl
    elif 26 <= nr_ppl <= 40:
        p_k2 += nr_ppl
    elif 41 <= nr_ppl:
        p_everest += nr_ppl

    all_ppl += nr_ppl

p_musala *= 100/all_ppl
p_monblan *= 100/all_ppl
p_kilimanjaro *= 100/all_ppl
p_k2 *= 100/all_ppl
p_everest *= 100/all_ppl

print(f'{p_musala:.2f}%')
print(f'{p_monblan:.2f}%')
print(f'{p_kilimanjaro:.2f}%')
print(f'{p_k2:.2f}%')
print(f'{p_everest:.2f}%')