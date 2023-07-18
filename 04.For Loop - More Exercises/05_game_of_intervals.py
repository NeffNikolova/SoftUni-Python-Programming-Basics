turns = int(input())

points = 0
p_10 = 0
p_20 = 0
p_30 = 0
p_40 = 0
p_50 = 0
invalid = 0

for i in range (turns):
    current_number = int(input())
    if current_number < 0 or current_number > 50:
        points *= (1/2)
        invalid += 1
    elif 0 <= current_number <= 9:
        p_10 += 1
        points += (current_number * 0.20)
    elif 10 <= current_number <= 19:
        p_20 += 1
        points += (current_number * 0.30)
    elif 20 <= current_number <= 29:
        p_30 += 1
        points += (current_number * 0.40)
    elif 30 <= current_number <= 39:
        p_40 += 1
        points += 50
    elif 40 <= current_number <= 50:
        p_50 += 1
        points += 100

print(f'{points:.2f}')
print(f'From 0 to 9: {(p_10 / turns * 100):.2f}%')
print(f'From 10 to 19: {(p_20 / turns * 100):.2f}%')
print(f'From 20 to 29: {(p_30 / turns * 100):.2f}%')
print(f'From 30 to 39: {(p_40 / turns * 100):.2f}%')
print(f'From 40 to 50: {(p_50 / turns * 100):.2f}%')
print(f'Invalid numbers: {(invalid/ turns * 100):.2f}%')