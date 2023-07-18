speed = float(input())

if speed <= 10:
    print('slow')
else:
    if 10 < speed  <= 50:
        print('average')
    else:
        if 50 < speed <= 150:
            print('fast')
        else:
            if 150 < speed <= 1000:
                print('ultra fast')
            else:
                print('extremely fast')