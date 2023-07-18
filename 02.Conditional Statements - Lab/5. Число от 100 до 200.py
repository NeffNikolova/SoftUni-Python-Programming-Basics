entry= int(input())

if entry < 100:
    print('Less than 100')
else:
    if 100<=entry<=200 :
        print('Between 100 and 200')
    else:
        if 200<entry:
            print('Greater than 200')