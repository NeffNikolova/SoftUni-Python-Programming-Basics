movie_name = input()
initial_seats = int(input())

nr_student = 0
nr_standard = 0
nr_kid = 0
all_movie_tickets = 0
taken_seats = 0

full = False

while movie_name != 'Finish':
    ticket_type = input()
    all_movie_tickets += 1
    if ticket_type == 'student':
        nr_student += 1
        taken_seats += 1
        if taken_seats == initial_seats:
            full = True
    elif ticket_type == 'standard':
        nr_standard += 1
        taken_seats += 1
        if taken_seats == initial_seats:
            full = True
    elif ticket_type == 'kid':
        nr_kid += 1
        taken_seats += 1
        if taken_seats == initial_seats:
            full = True
    elif ticket_type == 'End':
        all_movie_tickets -= 1
        full = True

    if full:
        print(f"{movie_name} - {(taken_seats/initial_seats*100):.2f}% full.")
        movie_name = input()
        if movie_name != 'Finish':
            initial_seats = int(input())
            taken_seats = 0
            full = False
        else:
            print(f"Total tickets: {all_movie_tickets}")
            print(f"{(nr_student/all_movie_tickets*100):.2f}% student tickets.")
            print(f"{(nr_standard/all_movie_tickets*100):.2f}% standard tickets.")
            print(f"{(nr_kid/all_movie_tickets*100):.2f}% kids tickets.")


