tournament_days = int(input())

wins_day = 0
losses_day = 0
money_day = 0
days_won = 0
days_lost = 0
money_all = 0

for day in range(tournament_days):
    sport = input()
    while sport != 'Finish':
        result = input()

        if result == 'win':
            wins_day += 1
            money_day += 20
        elif result == 'lose':
            losses_day += 1

        sport = input()

    if wins_day > losses_day:
        money_day *= 1.1
        days_won += 1
    else:
        days_lost += 1

    money_all += money_day
    wins_day = 0
    losses_day = 0
    money_day = 0

if days_won > days_lost:
    money_all *= 1.20
    print(f"You won the tournament! Total raised money: {money_all:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_all:.2f}")






