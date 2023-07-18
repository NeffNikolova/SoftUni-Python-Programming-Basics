months = int(input())

electricity_all = 0
water_all = months * 20
internet_all = months * 15
other_all = 0
other_mnt = 0

for i in range(months):

    electricity_mnt = float(input())

    electricity_all += electricity_mnt
    other_mnt = (electricity_mnt + 20 + 15) * 1.2
    other_all += other_mnt

print(f'Electricity: {electricity_all:.2f} lv')
print(f'Water: {water_all:.2f} lv')
print(f'Internet: {internet_all:.2f} lv')
print(f'Other: {other_all:.2f} lv')
print(f'Average: {((electricity_all + water_all + internet_all + other_all)/months):.2f} lv')