beginning = int(input())
ending = int(input())

for nr in range(beginning, ending + 1):
    nr_str = str(nr)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(nr_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(nr, end=' ')