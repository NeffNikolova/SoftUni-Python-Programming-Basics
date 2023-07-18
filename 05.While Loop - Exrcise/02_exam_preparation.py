max_unsatisfactory_grades = int(input())

nr_tasks = 0
average_grade = 0
last_task_name = ''
unsatisfactory_grades = 0
while True:
    task_name = input()
    if task_name == 'Enough':
        print(f"Average score: {(average_grade / nr_tasks):.2f}")
        print(f"Number of problems: {nr_tasks}")
        print(f"Last problem: {last_task_name}")
        break
    else:
        grade = int(input())
        nr_tasks += 1
        average_grade += grade
        last_task_name = task_name
        if grade <= 4:
            unsatisfactory_grades += 1
            if unsatisfactory_grades == max_unsatisfactory_grades:
                print(f"You need a break, {unsatisfactory_grades} poor grades.")
                break
