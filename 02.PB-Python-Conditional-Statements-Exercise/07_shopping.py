budget_peter = float(input())
videocards_nr = int(input())
processors_nr = int(input())
ram_nr = int(input())

difference = 0
total_spent = 0

videocard_price = 250
videocards_total = videocard_price * videocards_nr

processor_price = 0.35 * videocards_total
processors_total = processor_price * processors_nr

ram_price = 0.10 * videocards_total
ram_total = ram_price * ram_nr

if videocards_nr > processors_nr:
    total_spent = 0.85 * (videocards_total + processors_total + ram_total)
else:
    total_spent = videocards_total + processors_total + ram_total

if total_spent <= budget_peter:
    difference = budget_peter - total_spent
    print(f'You have {difference:.2f} leva left!')
else:
    difference = total_spent - budget_peter
    print(f'Not enough money! You need {difference:.2f} leva more!')

