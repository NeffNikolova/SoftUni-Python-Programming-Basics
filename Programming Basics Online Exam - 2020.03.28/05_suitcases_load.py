capacity = float(input())

suitcases = 0
end = False
no = False
while True:
    suitcase_volume = input()
    if suitcase_volume == 'End':
        end = True
        break
    else:
        suitcase_volume = float(suitcase_volume)
        suitcases += 1
        if suitcases % 3 == 0:
            suitcase_volume *= 1.1
            capacity -= suitcase_volume
        else:
            capacity -= suitcase_volume

        if capacity <= 0:
            suitcases -= 1
            no = True
            break

if end:
    print("Congratulations! All suitcases are loaded!")
elif no:
    print("No more space!")

print(f"Statistic: {suitcases} suitcases loaded.")