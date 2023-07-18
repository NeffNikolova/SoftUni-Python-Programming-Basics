nr_packs = int(input())

price = 0
microbus_t = 0
truck_t = 0
train_t = 0
all_weight = 0
for i in range (nr_packs):
    current_weight = int(input())
    all_weight += current_weight
    if current_weight <= 3:
        microbus_t += current_weight
        price += (current_weight * 200)
    elif 4 <= current_weight <= 11:
        truck_t += current_weight
        price += (current_weight * 175)
    elif current_weight >= 12:
        train_t += current_weight
        price += (current_weight * 120)

average_price = price/all_weight
p_microbus = microbus_t / all_weight * 100
p_truck = truck_t / all_weight * 100
p_train = train_t / all_weight * 100

print(f'{average_price:.2f}')
print(f'{p_microbus:.2f}%')
print(f'{p_truck:.2f}%')
print(f'{p_train:.2f}%')