from math import ceil

N_days = int(input())
M_kms = float(input())

all_kms = M_kms
daily_kms = M_kms

for day in range(N_days):
    increase_pr = int(input())
    increase_pr /= 100
    daily_kms *= (1 + increase_pr)
    all_kms += daily_kms

diff = abs(all_kms - 1000)

if all_kms >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers')

