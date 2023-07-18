entry = input()

prime_sum = 0
nonprime_sum = 0
dividers = 0

while entry != 'stop':
    entry = int(entry)
    if entry < 0:
        print("Number is negative.")
        entry = input()
        continue
    else:
        for n in range(2, entry + 1):
            if entry % n == 0:
                dividers += 1
        if dividers > 1:
            nonprime_sum += entry
        else:
            prime_sum += entry
        entry = input()
        dividers = 0
else:
    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {nonprime_sum}")
