
alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
c_count = 0
o_count = 0
n_count = 0
space = " "
word = ''
printable = ''

while True:
    current_letter = input()

    if current_letter == 'End':
        break
    elif current_letter.lower() not in alphabet_lowercase:
        continue
    elif current_letter == 'c':
        c_count += 1
        if c_count > 1:
            word += current_letter
    elif current_letter == 'o':
        o_count += 1
        if o_count > 1:
            word += current_letter
    elif current_letter == 'n':
        n_count += 1
        if n_count > 1:
            word += current_letter
    else:
        word += current_letter

    if c_count >= 1 and o_count >= 1 and n_count >= 1:
        c_count = 0
        o_count = 0
        n_count = 0
        printable += word
        printable += space
        word = ''

print(printable)

