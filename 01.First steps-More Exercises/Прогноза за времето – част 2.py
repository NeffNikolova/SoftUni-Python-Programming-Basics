temp = float(input())
statement = str()

if 26 <= temp <= 35:
    statement = 'Hot'
elif (20.1 <= temp <= 25.9):
    statement ='Warm'
elif (15 <= temp <= 20):
    statement ='Mild'
elif (12 <= temp <= 14.9):
    statement ='Cool'
elif (5 <= temp <= 11.9):
    statement ='Cold'
else:
    statement ='unknown'

print(statement)
