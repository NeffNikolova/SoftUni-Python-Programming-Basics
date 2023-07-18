N1 = int(input())
N2 = int(input())
operator = input()

result = 0
odd_even = None

if operator == "+":
    result = N1 + N2
    if result % 2 ==0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f'{N1} {operator} {N2} = {result} - {odd_even}')
elif operator == "-":
    result = N1 - N2
    if result % 2 ==0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f'{N1} {operator} {N2} = {result} - {odd_even}')
elif operator == "*":
    result = N1 * N2
    if result % 2 ==0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f'{N1} {operator} {N2} = {result} - {odd_even}')
elif operator == "/" and N2 != 0:
    result = N1 / N2
    print(f'{N1} / {N2} = {result:.2f}')
elif operator == "/" and N2 == 0:
    print(f'Cannot divide {N1} by zero')
elif operator == "%" and N2 != 0:
    result = N1 % N2
    print(f'{N1} % {N2} = {result}')
elif operator == "%" and N2 == 0:
    print(f'Cannot divide {N1} by zero')