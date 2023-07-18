while True:
    destination = input()
    if destination == "End":
        break
    else:
        min_budget = float(input())
        while min_budget > 0:
            savings = float(input())
            min_budget -= savings
            if min_budget <= 0:
                print(f'Going to {destination}!')