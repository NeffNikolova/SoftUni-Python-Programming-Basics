pool_volume_l = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
missing_time = float(input())
excess_water = 0

total_water = (debit_p1 + debit_p2) * missing_time
total_percent = total_water / pool_volume_l * 100

water_p1 = debit_p1 * missing_time
water_p1_percent = water_p1 / total_water * 100

water_p2 = debit_p2 * missing_time
water_p2_percent = water_p2 / total_water * 100

if water_p1 < pool_volume_l:
    print(f'The pool is {total_percent:.2f}% full. Pipe 1: {water_p1_percent:.2f}%. Pipe 2: {water_p2_percent:.2f}%.')
else:
    excess_water = (total_water - pool_volume_l)
    print(f'For {missing_time:.2f} hours the pool overflows with {excess_water:.2f} liters.')