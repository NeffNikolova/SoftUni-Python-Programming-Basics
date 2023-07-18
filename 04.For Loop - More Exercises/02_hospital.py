days = int(input())

docs = 7
treated =0
untreated =0

for i in range(1,days + 1):
    patients_daily = int(input())

    if i % 3 == 0:
        if untreated > treated:
            docs += 1

    if patients_daily > docs:
        untreated += (patients_daily - docs)
        treated += docs
    elif patients_daily <= docs:
        treated += patients_daily

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')