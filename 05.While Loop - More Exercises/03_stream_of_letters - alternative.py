#Stivi
final_word1 = []
current_word1 = []
c = 0
n = 0
o = 0
spase = 0
while True:
    word = input()
    if word == 'End':
        break
    else:
        if 65 <= ord(word) <= 90 or 97 <= ord(word) <= 122:
            if word == 'o' and o == 0:
                o += 1
            elif word == 'c' and c == 0:
                c += 1
            elif word == 'n' and n == 0:
                n += 1
            else:
                current_word1.append(word)
            if n == c == o == 1:
                final_word1.append(''.join(current_word1) + ' ')
                current_word1 = []
                n = 0
                c = 0
                o = 0

for i in final_word1:
    print(i, end="")