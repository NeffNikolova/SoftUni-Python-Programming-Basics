student_name = input()

failed = 0
average_grade = 0
year = 0

while True:
    grade = float(input())

    if grade < 4:
        failed += 1
        if failed == 2:
            print(f'{student_name} has been excluded at {year + 1} grade')
            break
    else:
        average_grade += grade
        year += 1

    if year == 12:
        print(f'{student_name} graduated. Average grade: {(average_grade / 12):.2f}')
        break
