bag_tax_over_20kg = float(input())
bags_kg = float(input())
days_until_travel = int(input())
bags_nr = int(input())

total_tax_bags = 0

bag_tax_up_to_10kg = bag_tax_over_20kg * 0.20
bag_tax_up_to_20kg = bag_tax_over_20kg * 0.50

if bags_kg < 10:
    if days_until_travel > 30:
        total_tax_bags = bag_tax_up_to_10kg * bags_nr * 1.10
    elif days_until_travel >= 7:
        total_tax_bags = bag_tax_up_to_10kg * bags_nr * 1.15
    elif days_until_travel < 7:
        total_tax_bags = bag_tax_up_to_10kg * bags_nr * 1.40
elif bags_kg <= 20:
    if days_until_travel > 30:
        total_tax_bags = bag_tax_up_to_20kg * bags_nr * 1.10
    elif days_until_travel >= 7:
        total_tax_bags = bag_tax_up_to_20kg * bags_nr * 1.15
    elif days_until_travel < 7:
        total_tax_bags = bag_tax_up_to_20kg * bags_nr * 1.40
elif bags_kg > 20:
    if days_until_travel > 30:
        total_tax_bags = bag_tax_over_20kg * bags_nr * 1.10
    elif days_until_travel >= 7:
        total_tax_bags = bag_tax_over_20kg * bags_nr * 1.15
    elif days_until_travel < 7:
        total_tax_bags = bag_tax_over_20kg * bags_nr * 1.40

print(f'The total price of bags is: {total_tax_bags:.2f} lv.')
