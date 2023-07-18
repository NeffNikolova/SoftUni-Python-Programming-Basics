nr_students = int(input())

p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
average = 0

for i in range(nr_students):
    current_grade = float(input())
    average += current_grade

    if current_grade < 3:
        p_2 += 1
    elif current_grade < 4:
        p_3 += 1
    elif current_grade < 5:
        p_4 += 1
    elif current_grade >= 5:
        p_5 += 1

print(f'Top students: {(p_5/nr_students*100):.2f}%')
print(f'Between 4.00 and 4.99: {(p_4/nr_students*100):.2f}%')
print(f'Between 3.00 and 3.99: {(p_3/nr_students*100):.2f}%')
print(f'Fail: {(p_2/nr_students*100):.2f}%')
print(f'Average: {(average/nr_students):.2f}')



