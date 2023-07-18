exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

full_exam_min = exam_hour * 60 + exam_min
full_arrive_min = arrive_hour * 60 + arrive_min
diff_min = abs(full_exam_min - full_arrive_min)
diff_hour = 0

early_late = None

if full_arrive_min < (full_exam_min - 30):
    early_late = "Early"
    if diff_min < 60:
        print(early_late)
        print(f'{diff_min} minutes before the start')
    if diff_min >= 60:
        diff_hour = diff_min // 60
        diff_min = diff_min % 60
        if diff_min < 10:
            print(early_late)
            print(f'{diff_hour}:0{diff_min} hours before the start')
        else:
            print(early_late)
            print(f'{diff_hour}:{diff_min} hours before the start')
elif (full_exam_min - 30) <= full_arrive_min <= full_exam_min:
    early_late = "On time"
    if full_arrive_min == full_exam_min:
        print(early_late)
    else:
        print(early_late)
        print(f'{diff_min} minutes before the start')
elif full_arrive_min > full_exam_min:
    early_late = "Late"
    if diff_min < 60:
        print(early_late)
        print(f'{diff_min} minutes after the start')
    if diff_min >= 60:
        diff_hour = diff_min // 60
        diff_min = diff_min % 60
        if diff_min < 10:
            print(early_late)
            print(f'{diff_hour}:0{diff_min} hours after the start')
        else:
            print(early_late)
            print(f'{diff_hour}:{diff_min} hours after the start')


