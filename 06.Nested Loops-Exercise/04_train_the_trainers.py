jury_nr = int(input())
presentation_name = input()
score = 0
avg_score = 0
all_score = 0
score_nr = 0

while presentation_name != 'Finish':
    for _ in range(jury_nr):
        score = float(input())
        avg_score += score
        all_score += score
        score_nr += 1
    avg_score /= jury_nr
    print(f'{presentation_name} - {avg_score:.2f}.')
    avg_score = 0
    score = 0
    presentation_name = input()
else:
    print(f"Student's final assessment is {all_score/score_nr:.2f}.")