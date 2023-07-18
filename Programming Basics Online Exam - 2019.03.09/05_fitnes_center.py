visitor_nr = int(input())

p_work_out = 0
p_protein = 0
n_back = 0
n_chest = 0
n_legs = 0
n_abs = 0
n_shake = 0
n_bar = 0

for _ in range(visitor_nr):
    activity = input()

    if activity == 'Protein shake' or activity == 'Protein bar':
        p_protein += 1
        if activity == 'Protein shake':
            n_shake += 1
        else:
            n_bar += 1
    if activity == 'Back' or activity == 'Chest' or activity == 'Legs' or activity == 'Abs':
        p_work_out += 1
        if activity == 'Back':
            n_back += 1
        elif activity == 'Chest':
            n_chest += 1
        elif activity == 'Legs':
            n_legs += 1
        elif activity == 'Abs':
            n_abs += 1

print(f"{n_back} - back")
print(f"{n_chest} - chest")
print(f"{n_legs} - legs")
print(f"{n_abs} - abs")
print(f"{n_shake} - protein shake")
print(f"{n_bar} - protein bar")
print(f"{(p_work_out * 100 / visitor_nr):.2f}% - work out")
print(f"{(p_protein * 100 / visitor_nr):.2f}% - protein")
