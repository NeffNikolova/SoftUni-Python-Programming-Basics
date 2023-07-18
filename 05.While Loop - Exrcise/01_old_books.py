favourite_book = input()

book_nr = 0

while True:
    book_name = input()

    if book_name == favourite_book:
        print(f'You checked {book_nr} books and found it.')
        break
    if book_name == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_nr} books.')
        break
    else:
        book_nr += 1
