hour = int(input())
minutes = int(input())

minutes_after_15 = minutes + 15

hour_new = 0
minutes_new = 0
hour_new_after_24 = 0

if minutes_after_15 >= 60:
   minutes_new = minutes_after_15 % 60
else:
    minutes_new = minutes_after_15

if (minutes_after_15 // 60) + hour >= 24:
     hour_new = (minutes_after_15 // 60) + hour - 24
else:
    hour_new = (minutes_after_15 // 60) + hour

if minutes_new < 10:
    print(f'{hour_new}:0{minutes_new}')
else:
    print(f'{hour_new}:{minutes_new}')
