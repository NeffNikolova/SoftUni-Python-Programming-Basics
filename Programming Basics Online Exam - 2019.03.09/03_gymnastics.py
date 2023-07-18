country = input()
tool = input()

score = 0

if country.lower() == 'russia':
    if tool.lower() == 'ribbon':
        score = 9.100 + 9.400
    elif tool.lower() == 'hoop':
        score = 9.300 + 9.800
    elif tool.lower() == 'rope':
        score = 9.600 + 9.000
elif country.lower() == 'bulgaria':
    if tool.lower() == 'ribbon':
        score = 9.600 + 9.400
    elif tool.lower() == 'hoop':
        score = 9.550 + 9.750
    elif tool.lower() == 'rope':
        score = 9.500 + 9.400
elif country.lower() == 'italy':
    if tool.lower() == 'ribbon':
        score = 9.200 + 9.500
    elif tool.lower() == 'hoop':
        score = 9.450 + 9.350
    elif tool.lower() == 'rope':
        score = 9.700 + 9.150

missing_percent = (1 - (score / 20)) * 100

print(f'The team of {country} get {score:.3f} on {tool}.')
print(f'{missing_percent:.2f}%')