beginning = int(input())
ending = int(input())
magic_number = int(input())
combination = 0
magic_a = 0
magic_b = 0
magic = False

while True:
    for a in range(beginning, ending + 1):
        for b in range(beginning, ending + 1):
            result = a + b
            combination += 1
            if result == magic_number:
                magic = True
                magic_a = a
                magic_b = b
                break
            else:
                continue
        if magic:
            break
        else:
            continue
    break

if magic:
    print(f"Combination N:{combination} ({a} + {b} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
