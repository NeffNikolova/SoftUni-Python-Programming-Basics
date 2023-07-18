budget = float(input())

name = input()
while name != "ACTION":
    if len(name) <= 15:
        payment = float(input())
    else:
        payment = budget * 0.2

    budget -= payment
    if budget <= 0:
        break
    else:
        name = input()

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")