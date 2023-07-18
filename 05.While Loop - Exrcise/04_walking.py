goal = 10000

diff = 0
while True:
    entry = input()

    if str(entry) == "Going home":
        steps_home = int(input())
        diff = abs(goal-steps_home)
        if steps_home < goal:
            print(f"{diff} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
    elif int(entry) > 0:
        goal -= int(entry)
        if goal <= 0:
            print("Goal reached! Good job!")
            print(f"{abs(goal)} steps over the goal!")
            break
        else:
            continue
