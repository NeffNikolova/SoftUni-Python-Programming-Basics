hour = int(input())
day = input()

if 10 <= hour <= 18 and (day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or
                         day.lower() == 'thursday' or day.lower() == 'friday' or day.lower() == 'saturday'):
    print('open')
else:
    print('closed')