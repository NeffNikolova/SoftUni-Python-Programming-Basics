n = int(input())
counter = 0
result = 0
for a in range(0,n + 1):
    for b in range(0, n + 1):
        for c in range(0, n + 1):
            result = a + b + c
            if result == n:
                counter += 1
print(counter)
