import sys

numbers = int(input())

oddsum = 0
oddmin = sys.maxsize
oddmax = -sys.maxsize
evensum = 0
evenmin = sys.maxsize
evenmax = -sys.maxsize

for i in range(1, numbers + 1):
    num = float(input())
    if numbers > 2:
        if i % 2 != 0:
            oddsum += num
            if num < oddmin:
                oddmin = num
                if num > oddmax:
                    oddmax = num
            elif num > oddmax:
                oddmax = num
                if num < oddmin:
                    oddmin = num
        elif i % 2 == 0:
            evensum += num
            if num < evenmin:
                evenmin = num
                if num > evenmax:
                    evenmax = num
            elif num > evenmax:
                evenmax = num
                if num < evenmin:
                    evenmin = num

    if numbers <= 2:
        if i % 2 != 0:
            oddsum += num
            oddmin = num
            oddmax = num
        elif i % 2 == 0:
            evensum += num
            evenmin = num
            evenmax = num

if numbers == 0:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif numbers == 1:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={oddsum:.2f},')
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
    print(f'EvenSum={evensum:.2f},')
    print(f'EvenMin={evenmin:.2f},')
    print(f'EvenMax={evenmax:.2f}')
